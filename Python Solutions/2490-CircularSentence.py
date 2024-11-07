class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        
        wordList = sentence.split()
        
        for i in range(len(wordList)):
            # Check if the end of the word is the same as the start of the next word
            if wordList[i][-1] != wordList[(i+1) % len(wordList)][0]:
                return False
            
        return True