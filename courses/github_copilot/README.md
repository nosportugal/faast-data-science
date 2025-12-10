# FAAST Advance Data Science - GitHub Copilot

![FAAST logo](/images/FAAST_preto.png)

Welcome to the Git repository for the "FAAST Advance Data Science - GitHub Copilot" learning path 🎉

This course is designed to introduce you to GitHub Copilot and teach you how to leverage AI-powered coding assistance effectively in your data science workflow.

The course is based on Microsoft's GitHub Copilot Fundamentals training paths, adapted for our team's specific needs and infrastructure requirements.

In this course, you'll learn:

- How to set up GitHub Copilot in your development environment, including VSCode Portable for on-prem infrastructure compatibility
- Core concepts and best practices for working with GitHub Copilot
- Prompt engineering techniques to get better results from Copilot
- Advanced features for code generation, refactoring, and testing
- How to develop unit tests using Copilot tools
- Optional, but ***encouraged***: How to use Model Context Protocol (MCP) to enhance Copilot capabilities with external context sources

## Learning Principles

This course follows the same principles established in the FAAST Advance Data Science program:

- Prefer self-directed learning over teacher-directed learning;
- Prefer content that's easily accessible (no paywalls or subscriptions);
- Prefer content that can be immediately applied;
- Always use code examples;
- Learning by teaching is encouraged.

## Learning Units

The course is structured in three main phases (modules):

### Setup & Introduction (~2-3 hours)
- **Setup Guide** (50-85 min): Installation and configuration of GitHub Copilot
  - Standard VSCode setup (15-30 min)
  - VSCode Portable setup for on-prem infrastructure requirements (30-45 min) - see [vscode_portable_setup.md](vscode_portable_setup.md)
  - GitHub Copilot extension activation (5-10 min)
- **[Introduction to GitHub Copilot](https://learn.microsoft.com/en-us/training/modules/introduction-to-github-copilot/)** (1-2 hours): Overview of GitHub Copilot capabilities and core concepts

### Module 1: GitHub Copilot Fundamentals (~1-2 hours)
- **[GitHub Copilot Across Environments: IDE, Chat, and Command Line Techniques](https://learn.microsoft.com/en-us/training/modules/github-copilot-across-environments/)** (~1 hour): Learn how to use Copilot in different environments and interfaces
- **[Introduction to prompt engineering with GitHub Copilot](https://learn.microsoft.com/en-us/training/modules/introduction-prompt-engineering-with-github-copilot/)** (~45 min): Master the art of crafting effective prompts to get the best results from Copilot

### Module 2: Advanced GitHub Copilot (~2-3 hours)
- **[Using advanced GitHub Copilot features](https://learn.microsoft.com/en-us/training/modules/advanced-github-copilot/)** (~1 hour): Explore advanced capabilities for code generation, refactoring, and documentation
- **[Develop unit tests using GitHub Copilot tools](https://learn.microsoft.com/en-us/training/modules/develop-unit-tests-using-github-copilot-tools/)** (~1.5 hours): Learn to create comprehensive test suites with AI assistance
  - **Except** the "Exercise - Develop unit tests using GitHub Copilot" and "Module assessment" section, which should be skipped, as it requires a C# installation.

### Module 3: Model Context Protocol (MCP) Exploration (~2 hours, advanced)

GitHub Copilot supports the Model Context Protocol (MCP), which allows you to extend Copilot's capabilities by providing additional context from external sources like databases, APIs, file systems, or GitHub repositories.

**What is MCP?**

MCP is an open protocol that enables AI assistants like GitHub Copilot to securely access contextual information from various sources. This helps Copilot provide more accurate and relevant suggestions based on your specific project context.

**GitHub MCP Server – key use cases**

The GitHub MCP Server is particularly useful for project management and development workflows. With it, you can:

- **Create and manage GitHub issues** directly from Copilot Chat
- **Open and refine user stories** with AI assistance, ensuring they are well-structured and complete
- **Search through repositories, pull requests, and issues** without leaving your IDE
- Access repository information, commits, and branches
- Streamline your development workflow by integrating GitHub operations into your coding environment

**Getting Started with MCP (as a user):**

1. **Install the GitHub MCP Server**: Follow the setup instructions at [github.com/github/github-mcp-server](https://github.com/github/github-mcp-server)
2. **Configure it in VSCode**: Connect the MCP server to GitHub Copilot Chat
3. **Explore practical use cases**: Try creating issues, refining user stories, or searching your repositories through natural language commands in Copilot Chat

**Resources:**

- [GitHub MCP Server Repository](https://github.com/github/github-mcp-server) - Installation and setup guide
- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [Extending GitHub Copilot Chat with MCP servers](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/extend-copilot-chat-with-mcp)
- [Using the GitHub MCP Server](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/use-the-github-mcp-server)

## Learning Structure

### Progress and Questions Tracking

In order to help mentors in tracking the progress of their mentees, we suggest using the following template:

- [Progress Question Tracking template](https://docs.google.com/spreadsheets/d/1nODnLBLCcC6Dqe_pK_bog-BA78E9AuUq1l4S81Px61w/edit?usp=sharing)

#### Tracking questions

Tracking questions is important so that we can improve the quality of the selected material, as well as create new ones.

We understand that some chapters might be really close, and students might want to ask questions directly to the mentor, but having the questions available publicly is to everybody's advantage.

### Initial Setup

Before starting the course, students must:

1. Complete the appropriate setup guide:
   - Standard VSCode installation, or
   - VSCode Portable installation (see [vscode_portable_setup.md](vscode_portable_setup.md) if you need on-prem compatibility)
2. Ensure GitHub Copilot is properly activated and working
3. Verify access to Microsoft Learn training modules

### Learning Unit Workflow

For each module:

1. **Review**: Go through the Microsoft Learn module at your own pace
2. **Practice**: Complete the hands-on exercises provided in the module
3. **Apply**: Try using the techniques learned in your own data science projects
4. **Reflect**: Document any challenges or insights in your progress tracking

Unlike traditional LDSSA learning units, these modules are completed directly on Microsoft Learn. There are no local notebooks to submit or grade.

## Expectations

### Expectations for students

Although we understand that time may be constrained, each student has responsibilities with their mentors, namely:

- Be open in your discussions with the mentor.
- Be courteous and respectful to your peers and mentor.
- Set your progress expectations with your mentor.
- Conduct yourself with integrity and honesty.
- Complete the Microsoft Learn modules and practice the techniques in real coding scenarios.
- Share your experience using GitHub Copilot with your peers.

### Expectations for mentors

A mentor is tasked with ensuring their peers become better professionals, as such, we expect them to:

- Reserve at least 30 minutes per week for the people you mentor, for answering questions and giving feedback.
- Encourage your mentee to communicate openly with you.
- Be courteous and respectful to your mentees.
- Keep track of questions and progress of the mentees (see [Progress tracking](#progress-and-questions-tracking))
- Conduct yourself with integrity and honesty.
- Share best practices and real-world examples of using GitHub Copilot effectively.

## Pre-requisites

In order to make the best use of this learning path, you should:

- Be comfortable with Python programming
- Have a GitHub account
- Have access to GitHub Copilot (individual, business, or enterprise license)
- Have VSCode installed (or be willing to set up VSCode Portable for on-prem requirements)

## Additional Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [GitHub Copilot for Business](https://resources.github.com/copilot-for-business/)
- [Best practices for using GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)
- [Model Context Protocol](https://modelcontextprotocol.io/)
