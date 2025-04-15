# Optimizing Context for GitHub Copilot

## Maximum Context Capacity

- Copilot can analyze multiple files and their relationships
- The context window varies by model but is typically several thousand tokens
- Code, comments, and documentation all contribute to the token count

### Ideal Context Structure

1. **Project Configuration**
   - Keep relevant project files open, like your `.csproj`:

   ````xml
   // filepath: d:\repros\Copilot-HowTo\source\C#\Copilot-C#.csproj
   <Project Sdk="Microsoft.NET.Sdk">
     <PropertyGroup>
       <TargetFramework>net8.0</TargetFramework>
       // ...existing code...
     </PropertyGroup>
     <ItemGroup>
       <PackageReference Include="Newtonsoft.Json" Version="13.0.3" />
       <PackageReference Include="NUnit" Version="4.3.2" />
     </ItemGroup>
   </Project>
   ````

2. **Code Structure Best Practices**

   ```csharp
   // Example of well-structured context
   /// <summary>
   /// Clear XML documentation
   /// </summary>
   public class MyClass
   {
       // Descriptive member names
       private readonly IMyDependency _dependency;

       // Clear method signature
       public async Task<Result> ProcessDataAsync(InputModel input)
   ```

### Tips for Optimal Results

1. **Keep Relevant Files Open**
   - Main file you're working on
   - Related interfaces/classes
   - Test files for the component
   - Project configuration files

2. **Prioritize Context**
   - Interface definitions
   - Class structure
   - Method signatures
   - Unit tests
   - Documentation

3. **Clean Context**
   - Remove commented-out code
   - Keep documentation up-to-date
   - Use consistent naming
   - Maintain clear file structure

4. **IDE Settings**
   - Pin important files in VS Code
   - Use workspace folders
   - Enable "Go to Definition" features

### What to Avoid

- Opening too many unrelated files
- Including large generated files
- Having multiple versions of similar code
- Keeping outdated comments

By following these guidelines, you'll help Copilot understand your codebase better and generate more accurate, contextually appropriate code suggestions.