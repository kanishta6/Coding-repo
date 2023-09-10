class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citationsAboveH = 0
        citationFrequencies = [0] * (len(citations)+1)

        for i in range(len(citations)):
            if citations[i] > len(citations):
                citationsAboveH += 1 
            else:
                citationFrequencies[citations[i]] += 1

        qualifyingPapers = citationsAboveH
        for h in range(len(citations), 0, -1):
            qualifyingPapers += citationFrequencies[h]
            if qualifyingPapers >= h:
                return h
        
        return 0