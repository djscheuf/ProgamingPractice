import unittest
import Infra.SimulationConductor as Sim

class SimulationConductorTest(unittest.TestCase):
    def setUp(self):
        self.SimC = Sim.SimulationConductor()

    def tearDown(self):
        del self.SimC

    def test_Constructor(self):
        #Arrange
        #Act
        simC = Sim.SimulationConductor()
        #Assert
        self.assertIsNotNone(simC)

    def test_InjectGameCount(self):
        #Arrange
        expected = 5
        #Act
        self.SimC.SetGameCount(expected)
        #Assert
        self.assertEqual(expected,self.SimC._finalGameCount)

    def test_InitGameCount(self):
        #Arrange
        #Act
        #Assert
        self.assertEqual(0,self.SimC._finalGameCount)

    def test_InjectPlayerStrategies(self):
        #Arrange
        expected = 
        #Act
        #Assert


if __name__ == '__main__':
    unittest.main()
