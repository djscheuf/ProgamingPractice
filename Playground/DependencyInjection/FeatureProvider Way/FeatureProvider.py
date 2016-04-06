__author__ = 'DJS'

'''
Feature Provider:
    Purpose: Provide Singleton-style access and DI to all system objects
    Usage:
        1. Call Provide() on the object you wish to provide. Indicate Title and value for the object
        2. Pass FeatureProvider to your DI class
        3. Access FeatureProvider by [] or by SafeRequest() passing the feature title(both, and an
            assertion method(safe)
'''

class FeatureProvider:
        def __init__(self):
            self.providers = {}

        def Provide(self, feature, provider, *args, **kwargs):
            if callable(provider):
                def call(): return provider(*args,**kwargs)
            else:
                def call(): return provider
            self.providers[feature] = call

        def __getitem__(self,feature): # allows the array access by [ ], where feature is the index.
            try:
                provider = self.providers[feature]
            except KeyError:
                raise KeyError("Unknown feature named %s" % feature)

            return provider()

        def SafeRequest(self,feature,assertion):
            obj = self.__getitem__(feature)

            assert assertion(obj), "The value %s of %s does not match the specified criteria" % (obj, feature)

            return obj

GlobalFeatureProvider = FeatureProvider() # provides global level access to Feature Provider.

if __name__ == '__main__':
    print("Sector: Feature Selector")
