# Clematis
Basic ZScript unit test framework for GZDoom \
Inspired by [Lilac](https://github.com/chesko256/Lilac) by [Chesko](https://github.com/chesko256)

## Documentation
### Making Test Suites
```CSharp
class ClematisExample : Clematis {
    override
    void TestSuites() {
        //////////////////
        // Assert-style //
        //////////////////

        Describe('Testing Player Stats');
            It('MaxHealth', AssertEval(20, '<', 100), LOG_Warning);
            It('Math', AssertEval(1+1, '==', 2), LOG_Fatal);
            It('Woot', Assert(true), LOG_Fatal);
        EndDescribe();

        let x = new('Object');
        let y = new('Object');

        Describe('Testing Math');
            It('Calculus', AssertFalse(0*1!=0), LOG_Error);
            It('Math', AssertSame(x, y, "Custom error message using values (%p and %p)"), LOG_Warning);
        EndDescribe();

        //////////////////
        // Expect-style //
        //////////////////

        Describe('Testing 123');
            It('Lorum', ExpectNum(12).to.be.lessThan().thisNum(30), LOG_Error);
            It('Ipsum', ExpectObj(new('Object')).to.be.instance().of.thisCls('Object'), LOG_Error);
            It('Call explicit matchers which can be added', ExpectNum(0, 'not >=').thisNum(42), LOG_Info);
        EndDescribe();
    }
}
```
Override TestSuites and put in your own!
Suites are started with `Describe` and end with `EndDescribe`

### How to Run Tests
#### On Instantiation
Tests run on instantiation by default, which can be disabled by overriding `Init()`
##### Factory Method
```CSharp
Clematis.Create('ClematisExample');
```
##### Network Event
```CSharp
EventHandler.SendNetworkEvent('test:ClematisExample');
```
##### Console Command
```
netevent test:ClematisExample
```
#### On Method Call
```CSharp
Clematis Tester=Clematis.Create('ClematisExample');
Tester.Run();
```

## License
Clematis is under the [BSD 3-Clause License](https://github.com/ZippeyKeys12/clematis/blob/master/LICENSE)
