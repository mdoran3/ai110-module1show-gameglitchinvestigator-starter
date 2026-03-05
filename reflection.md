# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  BUG 1 : The logic for "Go Lower" and "Go Higher" hints were reversed. For example,
          I entered 50 and the secret number was 15 and the hint it generated was
          "Go Higher".

  BUG 2 : The "New Game" button does not generate a new game - the attempts change 
          but not the game history

  BUG 3 : Changing the difficulty in the UI did not actually change the difficulty
          of the game. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude and copilot for autofill on comments. I also used the require 
streamlit and pytest modules. 

One AI suggestion that went well was changing the logic of "Too High" and "Too Low" for the hint. It understood the mistake and took action quickly.

An AI suggestion that needed additional prompting was the adjusting the difficulty. The difficulty logic was off a bit, but more importantly (and the AI did not get this at first) was that the program was not properly updating the difficulty based upon the user's selections and was instead hardcoding it. 

Both of these fixes were verified by creating pytests as well as by running the local instance and playing the game again. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    The tests were helpful but more over, physically opening the game and trying again was the best way. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
    With pytest I ran too high, too low, and winning scenarios to assert the proper result. For example:

      def test_guess_one_above_secret():
      outcome, _ = check_guess(6, 5)
      assert outcome == "Too High"

- Did AI help you design or understand any tests? How?
    Yes, I have done unit testing before and regression testing. I have never done it with pytest though so I needed to look up how to install it with AI. As far as Claude helping me understand the tests, I did not read its output and instead went adn read the tests in the file myself to see what types of cases were being tested. It seemed sufficient. 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
    Every new attempt at a guess, streamlit was rendering a new number. 

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
    When a user interacts with streamlit, it will rerun the entire codebase again, from top to bottom. So everytime a variable changes or something is added, the entire script is updated with this new change and completely rendered again. 

- What change did you make that finally gave the game a stable secret number?
    Conditional logic needed to be run that said if a secret was not already there, then it would render it again randomly based on the provided range, otherwise it would keep the secret variable. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
    Being more refined in the prompts with Claude and creating tests. 

  - This could be a testing habit, a prompting strategy, or a way you used Git.

- What is one thing you would do differently next time you work with AI on a coding task?
    Toggle between plan and agent mode more thoughtfully. 

- In one or two sentences, describe how this project changed the way you think about AI generated code.
    I have always known that it can create a mess. So I am taking away from this task that reviewing what the AI is doing is key. 