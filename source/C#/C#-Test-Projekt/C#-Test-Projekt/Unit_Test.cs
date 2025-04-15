using NUnit.Framework;

[TestFixture]
public class Tests
{

    [SetUp]
    public void Setup()
    {
    }

    [Test]
    public void Test1()
    {
        Assert.Pass();
    }

    [Test]
    public void TestNoArgs()
    {
        string[] args = new string[0];
        string result = Program.ProcessArguments(args);
        Assert.That("No arguments were passed", Is.EqualTo(result));
    }

    [Test]
    public void TestWithArgs()
    {
        string[] args = { "arg1", "arg2" };
        string result = Program.ProcessArguments(args);
        Assert.That("Arguments passed were: arg1, arg2", Is.EqualTo(result));
    }

}
