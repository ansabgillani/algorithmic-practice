from collections import Counter
import re

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        """
        Given a chemical formula as a string, return the count of each atom sorted by the atom name.
        
        Args:
        formula (str): The chemical formula string.

        Returns:
        str: The sorted chemical formula with counts.
        """
        stack = [Counter()]
        multipliers = []
        
        i = 0
        while i < len(formula):
            if formula[i] == '(':
                stack.append(Counter())
                multipliers.append(0)
            elif formula[i] == ')':
                top_counter = stack.pop()
                multiplier = multipliers.pop() + 1
                
                # If there's a number following the closing parenthesis, apply it as a multiplier
                if i + 1 < len(formula) and formula[i+1].isdigit():
                    num_end_index = re.search(r'\d+', formula[i+1:]).end() + i
                    multiplier *= int(formula[i+1:num_end_index])
                    i = num_end_index - 1
                
                for element, count in top_counter.items():
                    stack[-1][element] += count * multiplier
            elif formula[i].isupper():
                # Extract the atom name
                j = i + 1
                while j < len(formula) and formula[j].islower():
                    j += 1
                
                element = formula[i:j]
                i = j - 1
                
                # If there's a number following the atom, apply it as a multiplier
                if j < len(formula) and formula[j].isdigit():
                    num_end_index = re.search(r'\d+', formula[j:]).end() + j
                    stack[-1][element] += int(formula[j:num_end_index])
                    i = num_end_index - 1
            else:
                raise ValueError("Invalid character in the formula")
            
            i += 1
        
        final_counter = stack.pop()
        return ''.join(f"{atom}{final_counter[atom]}" if final_counter[atom] > 1 else atom for atom in sorted(final_counter.keys()))