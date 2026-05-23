## Task 1 - Imports

Brief: I practically had everything I needed already inside of Python, but decided to add a few extras.
What Claude (Copilot) Proposed: Perhaps adding `datetime` could add a bit of flair to the app?
What I Changed Before Approving: In addition to adding that library, I also imported `date` from said library as well as another library named `time`.
Verification: I ran `app.py` a few times to ensure there were no errors when compiling.
One Thing I Learned: To be honest, not much at this stage; everything is pretty self-explanatory.

## Task 2 - Getting Started

Brief: I only had one goal in mind: calculating sales tax, and calculating sales tax well.
What Claude (Copilot) Proposed: Have a main menu where the user could select a list of options.
What I Changed Before Approving: I scaled back the options to only two in order to keep things simple and to-the-point.
Verification: I tested multiple edge cases (e.g. typing in an invalid choice or a blank statement), then felt it ready to continue on.
One Thing I Learned: Keep it concise.

## Task 3 - Exit's To The Left

Brief: How would I "end" the program when prompted?
What Claude (Copilot) Proposed: Simply let the code end on its own without further programming.
What I Changed Before Approving: That seemed perfectly doable (you're doing nothing after all), but I added an extra "Thank You" message to end it off.
Verification: I simply went in and picked the "Exit" option, then determined that the code both outputted the thank you message as well as closed itself.
One Thing I Learned: It's alright to add a little bit more to make the program feel more lively.

## Task 4 - Calculations

Brief: How exactly will I go about accurately calculating sales tax?
What Claude (Copilot) Proposed: Get user input that restricts them to a certain number format to avoid miscalculations.
What I Changed Before Approving: I decided to make it so that any number entered would be in this relative format: "0.00" (i.e. two decimal places).
Verification: I tested a variety of numbers, and they all seemed to work well enough.
One Thing I Learned: Keep your program limited to one aspect at a time; don't overcomplicate what should be small in nature.

## Task 5 - Final Touches

Brief: Displaying the exact amount of money after tax: how do you do it effectively?
What Claude (Copilot) Proposed: Simply use a statement like this: `print(f"The total amount after tax is {<insert variable here>}")
What I Changed Before Approving: I added in some extra details and made sure that the final calculations were accurate to both the original price and the added sales tax.
Verification: Ran it, tested it, finished it.
One Thing I Learned: It's alright if it looks barebones at first; make it cool later.

## Task 6 - Final Touches?

Brief: All of that code was in a function: how do you display it well?
What Claude (Copilot) Proposed: Add an intro message and call the function right after.
What I Changed Before Approving: I added in the aforementioned date and formatted it in a neat and simple manner.
Verification: I ran the code and made sure that the intro message showed properly on-screen alongside the function to display the rest of the program.
One Thing I Learned: Make it exist first; you'll add the fine details later.

## AI Workflow

Due to the over simplicity of my program in terms of scope, I did not have a large range of tools that I felt compelled to switch between in order to accomplish specific tasks. However, I tried my best to give most of them an equal chance. For the most part, the code was assisted by Copilot, with it giving minor but immensely useful advice on where to direct my code. Claude, as I've stated previously in other modules, was a lot more useful as a back-burner: giving useful code to debug and implement, but not the end-all-be-all of my coding process.

## Reflection

1. It's no secret that AI agents are exceptional at cutting down on overall programming time; the amount of code that can be implemented in a program in a few swift keystrokes is immensely helpful. When it comes to my capstone project, with how short the completion process was, use of Copilot and Claude definitely made progression that much simpler.
2. In terms of a full-blown override, there weren't a terrible amount of incidents in which I had to completely stop Claude or Copilot in its tracks to prevent sloppily outputted code from injecting itself into my project. For the most part, my input came in the form of taking what Claude or Copilot would describe to me, refining it, and applying it to my program. I would say that, thanks in part to my `CLAUDE.md` file, me and Claude were on the same page, while Copilot needed a little more direction in order to give optimal output.
3. I chose a project that I knew would be something that everyone would be willing to use--after all, nobody likes accounting for sales tax--and tried my hardest to make it as accessible as possible whilst keeping it in the range of my expertise. Because of this, I decided to make it a CLI-focused program to cut down on complexity and amplify simplicity alongside giving said program an easy-to-use, accessible input process designed for quick use. In the future, I would love to revisit this and other similar ideas and make them slightly more aesthetically pleasing and include more features that expand on my original ideas.
4. With the workflow I've learned throughout this module, I believe that I'll be able to tackle AI with the mindset of a tool and not a crutch or an end-all-be-all of my programming prowess. Day one, I'll show that I'm willing to apply myself and learn even more than what I've learned here.
