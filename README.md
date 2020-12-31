# Sqlite3 and Code Quality Project

#### Style
1. Comments
    * analysis:
        * useless commented codes make people confused and hard to understand
        * no comment and docstrings to help to understand codes 
    * change:
        * delete all the useless commented codes
        * add docstrings and some useful comments that help to read and understand codes
    
2. Naming Conventions
    * analysis:
        * too many meaningless variable names and abbreviations
        * hard to understand codes
    * changes:
        * refactor all the short variable names like 'c', 'b', 'd' to meaningful names
            * c to cursor
            * b to body
            * d to description
            * q to query
        * refactor all the variable names that hard to understant like 'lspos', 'p_full' to names that easy to understand 
            * lspos to pso_from_tail
            * p_crs to parse_createchannel
            * p_ul to parse_parsetopspam
            * p_gts to parse_gettopspam
            * p_full to parse_storechatlog
            * p_qr to parse_querychatlog
        * refactor all abbreviations to full names that easy to understand  

3. Long sentence(more than 80)
    * analysis: 
        * should fits to screens
    * changes:
        * enter new line
    
4. Assignment can be replaced with augmented assignment like fragment = fragment + " = "
    * analysis:    
        * not a good style
    * changes:
        * refactor to fragment += " = "

#### Structure
* analysis:
    * have too many responsibilities in one function
    * for a function, it's too long and not clear
    * not a OO design, hard to write unit test or add extensibility, also not a nice design for debugging
    * hard to understand
* change:
    * Create a class named Twitch
        * easy to understand
        * easy to write unit test
    * seperate main function to 5 small functions and store them in class Twitch, since one function should handle only one responsibility 
    * delete main function and remove all the executions to if __name__ == "__main__":

#### Error Handling
* analysis:
    * for the data base access, we should do the error handling by using the default error handler in the sqlite3
* changes:
    * add try catch for every data base access.

#### Logging
* analysis:
    * choose logging instead of print, we can
        * define what types of information you want to include in our logs
        * set the destination for out logs
* changes:
    * init a log by using logging.getLogger(__name__)

#### Extensibility
* analysis:
    * the starter code is not possible to add any functionality or extensibility
    * we choose use superclass and subclass for it, which is easy to add function or other streaming platform for future
    * also easy to avoid duplicate codes for future
    * this design fits the OO design
* changes:
    * Create a abstract superclass for extensibility, easy to add more functionalities, streaming platform and reduce duplicate codes
    * Refactor operation list to a Hashmap to easy to add more operations

#### Object Orientation
* analysis:
    * For OO design, 
        * it's easier to maintain objects
        * objects may be understood as stand-alone entities
        * objects are appropriate reusable components
        * it's easier to write unit test
        * it's easier to understand for people read this codes later
        * it's more logical
* changes:
    * Use a abstract superclass and subclass instead of the single function
    * Use DAO design partern and alos apply class-base for DAO

#### Testing DAO
* analysis:
    * there is no testing case written for DAO. We will give a testing file dao_test.py for dao.py for the superclass and
      all its subclasses
* change:
    * create a SuperTestclass named SuperDaoTestCase
    * create classes of all subclasses one for each DAO class
* goal
    * run all the test classes and get 100% coverage

#### Testing twitch
* analysis:
    * there is no testing case written for twitch. We will give a testing file twitch_test.py for twitch.py of
    the wrapped superclass all its subclasses and all it's method
* change:
    * create a SuperTestclass named SuperTwitchTestCase
    * create classes of all subclasses one for Twitch Testing class
* goal
    * run all the test classes and get 100% coverage



