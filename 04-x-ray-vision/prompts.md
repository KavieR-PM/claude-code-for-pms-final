# 04 · X-Ray Vision — prompts

**Context:** You joined Rook two weeks ago as PM on Dispatch.
Release 4.2 shipped on 12 August, just before you arrived, and
landed badly. Last session the numbers showed you what happened: a
ping used to wait ninety seconds and now it waits sixty, people
missed pings they used to catch, and missing one counts the same as
turning one down — so four responders stopped hearing from us
altogether.

At the end of the session, ask Claude Code to save the prompts you
wrote yourself below — not the starter prompt. The closing slide has
the exact prompt to paste. By Module 6 this file is a prompt library
built from your own questions.

---

### 1.
This is interesting, how do you think this could infer what we saw from some of the data analysis?

### 2.
add this to the synthesis file but before you do so, give me the quick tldr on what we need to do next

### 3.
do we have the real location/travel time data?

### 4.
do we have any information in the repo that can help us?

### 5.
give me a tour of the python files

### 6.
Based on what we now know after reviewing the code, help me create hypothesis statements that we should go test. Rank the hypothesis based on how likely we're able to identify the root cause.

### 7.
Add another column that will give a brief 1 sentence explanation on why we recommend # 1 and #2 over the others. Give me some data that will support the recommendation

### 8.
rewrite the hypothesis statement using scientific method framing

### 9.
include the rewritten hypotheses in the table. The columns should be hypothesis, If/Then/Because, Confirms if, Fails if, Likelihood of resolving

### 10.
add it to the synthesis file

### 11.
commit and push

### 12.
Marcus our engineering manager is asking 

Quick one, did the change to who gets asked first apply to responders who'd already been turning jobs down, or just new ones? Can't tell from the code and don't want to guess on this. Anyone know?

### 13.
What hypothesis would otherwise confirm this?

### 14.
yes redraft the slack message to marcus with this info

### 15.
yes add #11 to the hypotheses table in the synethesis file

### 16.
Can we confirm nothing changed in the code pre 4.2? Is it really just configs?

### 17.
From your point of view, what should we do next?

### 18.
let's send the message to Marcus on the Slack channel

### 19.
Find me the part of this code that takes points off somebody when they miss a ping or turn one down. Show it to me and explain it in plain English. Then find me every single thing in this code that puts points back on.

### 20.
add this to the synthesis file

### 21.
commit and push

### 22.
According to my findings in the code, for someone who's gone quiet, they need to  _________ 

Fill in the blank

### 23.
paste this whole message to the slack channel https://app.slack.com/client/T0A93EN1Y/C0B8LTV13EJ

### 24.
not yet

### 25.
looking at the repo, what were the specific requirements for 4.2 and was it implemented per spec?
