import itertools
import random
from copy import deepcopy
from time import perf_counter

class SudokuSolver:
    
    def __init__(self, puzzle, step_limit = 10, variablePickingApproach = "MCV", rules = list(range(1, 7))):

        self.rule_mapping = {1: self.naked_singles, 2: self.hidden_singles, 3: self.nakedK, 4: self.hidden_pairs, 5: self.nakedK, 6: self.hidden_triples}
        self.puzzle = puzzle
        self.domains = self.init_domain(puzzle)
        self.variablePickingApproach = variablePickingApproach
        self.rules = rules
        self.step_limit = step_limit

        self._baseline_x = 0
        self._baseline_y = 0
        self.btCount = 0
        self.rule_counter = {x:0 for x in range(1, 7)}
        self.solution = None

    def init_domain(self, puzzle):
        domains = []
        for i, row in enumerate(puzzle):
            domain = []
            for j, digit in enumerate(row):
                if(digit == '0'):
                    domain.append([str(x) for x in range(1, 10) if str(x) not in self.neighbor_values((i, j))])
                else:
                    domain.append([digit])
            domains.append(domain)
        return domains

    def neighbor_values(self, point):
        r, c = point
        values = []
        for (r,c) in self.neighbor_points(point):
            values.append(self.puzzle[r][c])
        return values

    def neighbor_points(self, point):
        r,c = point
        points = set()
        for i in range(len(self.puzzle)):
            points.add((r,i))
            points.add((i, c))
        for p in map(lambda x: (x[0] + ((r//3) * 3), x[1] + ((c//3) * 3)), itertools.product(range(0, 3), repeat=2)):
            points.add(p)
        points.remove(point)
        return points

    def isSolved(self, domains):
        if(domains == False):
            return False
        for i in range(len(domains)):
            for j in range(len(domains[0])):
                if(len(domains[i][j]) != 1):
                    return False
        return True

    def hidden_singles(self, domains, changed):
        for i, row in enumerate(domains):
            for j, domain in enumerate(row):
                hidden_single = set(domain) - set(self.neighbor_values((i,j)))
                if(len(hidden_single) == 1 and len(domain) != 1):
                    domains[i][j] = list(hidden_single)
                    changed = True
        return domains, changed

    def hidden_pairs(self, domains, changed):
        for i, row in enumerate(domains):
            for j, domain in enumerate(row):
                for (neighbor_x, neighbor_y) in self.neighbor_points((i,j)):
                    neighbor_domain = domains[neighbor_x][neighbor_y]
                    hidden_pair = set(domain) - set(neighbor_domain)
                    if(len(hidden_pair) == 2 and (len(domain) > 2 and len(neighbor_domain) > 2)):
                        domains[i][j] = list(hidden_pair)
                        domains[neighbor_x][neighbor_y] = list(hidden_pair)
                        changed = True
                        
        return domains, changed
	

    def hidden_triples(self, domains, changed):
        for i, row in enumerate(domains):
            for j, domain in enumerate(row):
                for (neighbor_x, neighbor_y) in self.neighbor_points((i,j)):
                    neighbor_domain = domains[neighbor_x][neighbor_y]
                    hidden_pair = set(domain) - set(neighbor_domain)
                    if(len(hidden_pair) == 3 and (len(domain) > 3 or len(neighbor_domain) > 3)):
                        domains[i][j] = list(hidden_pair)
                        domains[neighbor_x][neighbor_y] = list(hidden_pair)
                        changed = True
        return domains, changed

    def naked_singles(self, domains, changed):
        for i, row in enumerate(domains):
            for j, domain in enumerate(row):
                if(len(domain) == 1):
                    for (neighbor_x, neighbor_y) in self.neighbor_points((i,j)):
                        prev_length = len(domains[neighbor_x][neighbor_y])
                        domains[neighbor_x][neighbor_y] = list(set(domains[neighbor_x][neighbor_y]) - set(domain))
                        if(prev_length != len(domains[neighbor_x][neighbor_y])):
                            changed = True
        return domains, changed

    def nakedK(self, domains, k, changed):
        for i, row in enumerate(domains):
            for j, domain in enumerate(row):
                if(len(domain) == k):
                    for (neighbor_x, neighbor_y) in self.neighbor_points((i,j)):
                        prev_length = len(domains[neighbor_x][neighbor_y])
                        domains[neighbor_x][neighbor_y] = list(set(domains[neighbor_x][neighbor_y]) - set(domain))
                        if(prev_length != len(domains[neighbor_x][neighbor_y])):
                            changed = True
        return domains, changed

    def solve(self):
        if self.solution:
            return self.solution
        
        start_time = perf_counter()
        self.domains = self.recursiveBacktracking(self.domains)
        end_time = perf_counter()
        self.solution = {"isSolved" : self.isSolved(self.domains), "domains": self.domains, "btCount": self.btCount, "rule_counter" : self.rule_counter, "time_taken":end_time - start_time}
    
        return self.solution

    def recursiveBacktracking(self, domains):

        if self.isSolved(domains):
            return domains
        if(self.step_limit == self.btCount):
                return False
        self.btCount += 1

        variable = self.choose_variable(domains)
        if(variable == False):
            return False
        v_x, v_y = variable

        for value in domains[v_x][v_y]:
            new_domains = deepcopy(domains)
            new_domains[v_x][v_y] = [value]
            new_domains = self.constraintPropagation(new_domains)
            if self.rules == []:
                result = self.recursiveBacktracking(new_domains)

            if new_domains is not False:
                result = self.recursiveBacktracking(new_domains)

                if result is not False:
                    return result
        
        return False

    def constraintPropagation(self, domains):
        changed = True
        steps = 0
        while changed:
            changed = False
            for r in self.rules:
                rule = self.rule_mapping[r]
                if r in [3, 5]:
                    k = (2 if (r == 3) else 3)
                    (domains, changed) = rule(domains, k, changed)
                else: 
                    (domains, changed) = rule(domains, changed)

                if changed:
                    self.rule_counter[r] += 1
                    break
        return domains 
    
    def choose_variable(self, domains):
        if self.variablePickingApproach == "baseline":
            return self.baselineOrdering(domains)
        else:
            return self.MCV(domains)
        
    def MCV(self, domains):
        print("hello")
        minLength = 10
        mcvs = []
        for i, row in enumerate(domains):
            for j, domain in enumerate(row):
                length = len(domain)
                if length < minLength and length > 1:
                    minLength = length

        for i, row in enumerate(domains):
            for j, domain in enumerate(row):
                if(len(domain) == minLength):
                    mcvs.append((i,j))

        if(len(mcvs) == 0):
            return False
        mcv = random.choice(mcvs)
        print(mcv)
        return mcv

    def baselineOrdering(self, domains):
        x,y = self._baseline_x, self._baseline_y
        self._baseline_y = (self._baseline_y + 1) % 9
        if (self._baseline_y == 0):
            self._baseline_x = (self._baseline_x + 1) % 9

        return (x,y)
    
    def print_board_from_domains(self, domains):
        if(self.isSolved(domains)):
            for i, row in enumerate(domains):
                if(i % 3 == 0):
                    print()
                for j, domain in enumerate(row):
                    if(j %3 == 0): print(" ", end = "")
                    print(*domain, end = "")
                print()
        else:
            print("SuDoKu not solved")

