class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        asteroids.sort()
        for e in asteroids:
            if e<=mass:
                mass+=e
            else:
                return False
        return True 
