* Environment Setup:
After a good deal of trouble with the unittest imports, I finally created symbolic links in the testing directories for ease of use!

**How to:
+ In terminal: Navigate to Test Directory
+ enter command: ln -s ../../<Package of interest>
+ In TestClass: 'from <package>.<class or subpackage> import *' now works

* IMPORTANT: This tech trick may mean that the tests are not compatible with windows machines.
+ This assumes, that Windows machines don't support symbolic links. OSX, I think, should be fine.
