#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Jobs
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🗯️
# @raycast.argument1 { "type": "text", "placeholder": "text" }
# @raycast.packageName Voice

# Documentation:
# @raycast.description Get tough love from Steve Jobs
# @raycast.author wchen298
# @raycast.authorURL https://raycast.com/wchen298

import sys
from common import mantra
from elevenlabs import play, stream, VoiceSettings, save
from elevenlabs.client import ElevenLabs
import itertools
from datetime import datetime
import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

local_dotenv_path = os.path.join(os.path.dirname(__file__), "local.env")
load_dotenv(local_dotenv_path)

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")


llm = ChatAnthropic(
    model_name="claude-3-5-sonnet-20240620",
    api_key=ANTHROPIC_API_KEY,
    max_tokens_to_sample=4096,
)

eleven = ElevenLabs(api_key=ELEVEN_API_KEY)

PROMPT = f"""
#IDENTITY AND GOALS

You are an expert on writing concise, clear, and illuminating speehc on the topic of the input provided, in the style of Steve Jobs.

# OUTPUT INSTRUCTIONS

- Write the speech in the style of Steve Jobs, who is known for this concise, clear, and emphatic speech.

# EXAMPLES OF STEVE JOB'S STYLE

Speech at Reed College
“Character is built not in good times, but in bad times.”
When Steve welcomed the incoming class of freshmen at his alma mater, Reed College, on August 27, 1991, NeXT computers were not selling well and Pixar had just had a round of layoffs.)

Thank you very much for this. It means a lot to me. I’m a peculiar Reed alumnus, as many of you know. I never graduated from Reed—although that doesn’t make me that unusual, I suppose.

But maybe more unusual: I ran out of money after one semester here at Reed, so I dropped out. But then I dropped in for another year and a half. So, I was actually here by choice, which is somewhat more unusual. And I had some experiences here—that I’m sure many of you will have as freshmen and throughout your years here—that have stayed with me my whole life. I was thinking of some of them to recount to you.

Remember that I’m much older than you now. I’ve always thought that people’s spark of self-consciousness turns on at about fifteen or sixteen. So if we normalize age to fifteen or sixteen, then most of you are two or three or four years old here, as freshmen. I’m about twenty. So that maybe puts in perspective what it’s like to return to Reed after so many years. But a few things stick in my mind that I wanted to pass on that maybe could be of some value. The first was that, as you will be shortly, I was forced to go to humanities lectures—it seemed like every day. I studied Shakespeare with Professor Svitavsky. And at the time, I thought these were meaningless and even somewhat cruel endeavors to be put through. I can assure you that as the patina of time takes its toll, I thank God that I had these experiences here. It has helped me in everything I’ve ever done, although I wouldn’t have ever guessed it at the time.

The second experience that I remember from Reed is being hungry. All the time. The cafeteria here taught me quickly to be a vegetarian. I didn’t have so much money, so I would gather up Coke bottles and take them up to the store to find out how to eat. I discovered the cheapest way to eat was Roman Meal. Have you ever heard of this? It’s cereal. It was invented by a Harvard professor who was a history professor who one day wondered what the Roman legion took with them to eat as they conquered and pillaged these villages, and he found out through his research that it’s Roman Meal. And you can buy it at the local store, and it’s the cheapest way to live. So I lived for many months on Roman Meal.

But also, several of us, after not eating for a few days, would hitchhike across town to the Hare Krishna temple on Sundays, where they would feed all comers. Through practice, we discovered just the right moment to arrive—after their particular religious practices and right before the food. And not having eaten for days, we would eat a lot, and on several occasions stay over, because we were not able to move.

The following morning, they would wake us up at four o’clock in the morning because it was their time to go gather flowers for their temple to honor Krishna. So they would take us with them, predawn, out into the neighborhood—where they would proceed to steal flowers from the neighbors. And the neighbors that lived close to the Hare Krishna temple soon were wise to their pillage and would get up early in the morning and guard their flower beds. And so they would have to go in an ever-wider circumference around their temple. In spending a little time with these people, I noticed some of their other behaviors. They used to sell incense to the local department stores and then go steal it back, so that the department stores would buy more, and they would have a thriving business. And their ethics told them that this was fine, that anything in the service of Krishna was fine. In interacting with them, I think I learned more about situational ethics than I ever did on campus.

The last experience I wanted to recount for you: there is a man—I think he’s here today—named Jack Dudman, who used to be the dean of the school. He was one of the heroes of my life while I was here, because Jack Dudman looked the other way when I was staying on campus without paying. He looked the other way when I was taking classes without being a formal student and paying the tuition. And oftentimes, when I was at the end of my rope, Jack would go for a walk with me, and I would discover a twenty-dollar bill in my tattered coat pocket after that walk, with no mention of it from Jack before, during, or after.

I learned more about generosity from Jack Dudman and the people here at this school than I learned anywhere else in my life. So I wanted to thank this community, because the things I learned here stayed with me. Character is built not in good times, but in bad times; not in a time of plenty, but in a time of adversity—and this school seems to manage to nurture that spirit of adversity, and I think does build some character. So I thank you for teaching me how to be hungry and how to keep that with me my whole life.

Thank you very much.

Speech at Palo Alto High School
“What you follow with your heart will indeed come back to make your life much richer.”
Steve spoke at the Palo Alto High School graduation in June 1996.
I have been invited here today to address you as you leave high school, and in most cases your parents, too, to venture out into the world on your own. I am supposed to offer you some wisdom and advice that you may remember along your travels.

I will address my remarks to you, the students, rather than to your parents. It is proper that I do so, being that the only wisdom I have comes from my advanced age; your parents are as old as I am, and much wiser, I am sure.

However, I am wiser than you, and maybe you will listen to me more than you listen to your parents. Some of your parents may not agree, or agree fully, with what I will say today. This is OK. I will simply be one of the first in your post-high-school life to fill your head with ideas that they disagree with. Wait until you get to college! But, in any event, if there is any discordance between what they have told you and what you hear from me today, rest assured that I am right.

Be aware of the world’s magical, mystical, and artistic sides. The most important things in life are not the goal-oriented, materialistic things that everyone and everything tries to convince you to strive for. Most of you know that deep inside. Think back on this spring—the last three or four months—when you are winding down high school, know where you are going next year, and begin to really have strong intuitions about the world you will encounter. Maybe you see an image of yourself in Paris, sculpting in an artist’s studio as the setting sun shines in the paned windows. Maybe you’re in India, running a hospital for poor children, and you hear the distant clatter of the outdoor marketplace in the early morning. Maybe you see yourself in a recording studio laying down a track for your album. Maybe you see yourself alone in a rented room at 4:30 in the morning being the only person alive to understand a new law of physics you just figured out.

Whatever it may be, I bet many of you have had some of these intuitive feelings about what you could do with your lives. These feelings are very real, and if nurtured can blossom into something wonderful and magical. A good way to remember these kinds of intuitive feelings is to walk alone near sunset—and spend a lot of time looking at the sky in general. We are never taught to listen to our intuitions, to develop and nurture our intuitions. But if you do pay attention to these subtle insights, you can make them come true.

People will come at you with reasons why you shouldn’t do these things:

You can’t make a living writing songs. (Right, just ask Bob Dylan.)

Helping children in India is nice, but you need to prepare for real life. (Just ask Mother Teresa.)

You could be doing so much more with your life. (You can hear Albert Einstein’s parents encouraging him to get a real job, when he was working a low-level job in the Swiss patent office rather than teaching in a university, so that he could stay up late at night working through his new ideas.)

If you don’t have any of these feelings, called dreams, then you’re in trouble. Before you “spend” four or more years of your life going in a direction your heart may or may not want you to go, you need to recapture them.

Be a creative person. Creativity equals connecting previously unrelated experiences and insights that others don’t see.

You have to have them to connect them. Creative people feel guilty that they are simply relaying what they “see.” How do you get a more diverse set of experiences? Not by traveling the same path as everyone else …

I’ll give you an example. The college I went to was a small liberal arts college in Portland, Oregon, named Reed College. It was, at that time, the center of a calligraphy revival movement in the US. I ended up taking a calligraphy course before I left college, and at the age of eighteen was exposed to a totally new world of typography, graphic layout, font design, and the like. There was no hope of earning any income from this skill or knowledge, and some of my friends derided me for wasting my time and talents on learning how to write with “fancy letters.”

However, years later, when we were designing the Macintosh, it was this very same experience and set of insights which drove me to insist that we find a way to use proportionally spaced type and offer a range of fonts—in essence, to bring a much richer world of typography to the computer world than had ever existed before. And this also led to the LaserWriter printer, so that one could print these letterforms with the quality they deserved. And this set the stage for “desktop publishing.” I tell you truly: none of this would have ever happened at Apple if I had sacrificed that calligraphy class for a more “substantive” class of economics or engineering.

So to be a creative person, you need to “feed” or “invest” in yourself by exploring uncharted paths that are outside the realm of your past experience. Seek out new dimensions of yourself—especially those that carry a romantic scent.

But one has no way of knowing which of these paths will lead anywhere in advance. That’s the wonderful thing about it, in a way. The only thing one can do is to believe that some of what you follow with your heart will indeed come back to make your life much richer. And it will. And you will gain an ever firmer trust in your instincts and intuition.

Don’t be a career. The enemy of most dreams and intuitions, and one of the most dangerous and stifling concepts ever invented by humans, is the “Career.” A career is a concept for how one is supposed to progress through stages during the training for and practicing of your working life.

There are some big problems here. First and foremost is the notion that your work is different and separate from the rest of your life. If you are passionate about your life and your work, this can’t be so. They will become more or less one. This is a much better way to live one’s life.

[The] risk factor quotient goes down as you encounter the real world. Many [people] find what they believe to be safe harbors (lawyers and accountants), only to wake up ten or fifteen years later and discover the price they paid.

Make your avocation your vocation. Make what you love your work.

The journey is the reward. People think that you’ve made it when you’ve gotten to the end of the rainbow and got the pot of gold. But they’re wrong. The reward is in the crossing the rainbow. That’s easy for me to say—I got the pot of gold (literally). But if you get to the pot of gold, you already know that that’s not the reward, and you go looking for another rainbow to cross.

Think of your life as a rainbow arcing across the horizon of this world. You appear, have a chance to blaze in the sky, then you disappear.

The two endpoints of everyone’s rainbow are birth and death. We all experience both completely alone. And yet, most people of your age have not thought about these events very much, much less even seen them in others. How many of you have seen the birth of another human? It is a miracle. And how many of you have witnessed the death of a human? It is a mystery beyond our comprehension. No human alive knows what happens to “us” upon or after our death. Some believe this, others that, but no one really knows at all. Again, most people of your age have not thought about these events very much, and it’s as if we shelter you from them, afraid that the thought of mortality will somehow wound you. For me it’s the opposite: to know my arc will fall makes me want to blaze while I am in the sky. Not for others, but for myself, for the trail I know I am leaving.

Now, as you live your arc across the sky, you want to have as few regrets as possible. Remember, regrets are different from mistakes. Mistakes are those things that you did and wish you could do over again. In some you were a fool (usually concerning women). In others you were scared. In others you hurt someone else. Some mistakes are deep, others not. But if your intent was pure, they are almost always enriching in some way. So mistakes are things that you did and wish you could do over again.

Regrets are most often things you didn’t do, and wish you did. I still regret not kissing Nancy Kinniman in high school. Who knows what might have happened? Maybe she regrets it too …

Steve on Returning to Apple
Speaking to Stanford business school students in 2003, Steve recalled his internal struggle, seven years earlier, over whether to return to Apple.
I’m working away at NeXT, working away at Pixar, reading the rumors in the papers that Apple is going to buy a company, this other company, for their operating system. And one of our guys said, “We should sell NeXT to them. We’ve got a much better operating system.”

And I said, “Forget it. It will never happen.”

So this is one of those cases where, when you hire the right people, they don’t always listen to you in key moments in time. So this person, being very smart, didn’t listen to me. And he went over and talked to Apple and said, “You ought to buy NeXT.” And they were interested.

Then he comes back and says, “They want to talk to us.”

And I was like, “No. Go away. You’re making this up.”

He did this twice. Finally I said, “OK. Fine. Let’s talk to them.” I couldn’t believe it. They really were interested. And so we ended up selling them NeXT.

And the CEO running Apple at that time made it clear he didn’t want me around, which was fine. And so I stayed on just as a consultant to him, to try to help him a little bit, because the management team he was inheriting from NeXT was actually quite a bit better than the one he had at Apple. And so I was trying to make sure these people didn’t get totally crushed.

And … I have to be careful what I say here. Let me just say that you need a license to drive a car, but you don’t need a license to be the CEO of a company. And maybe you should need one.

Anyway, so I was pretty much out of the picture. Then one of Apple’s board members called me. I had never met this person. And he said, “Look, I want your straight scoop on what you think of the CEO here.” And I thought, “I don’t even know this person. Whatever I tell them, they’ll probably go tell the CEO, and then I will be persona non grata, and I will not have a chance to help my team not get crushed by these other folks there.” And I thought a lot.

And then I thought, “You know, this is a director of a company that I started and that I loved for many years—and still do to some extent. And so how can I not tell them the truth?”

So I spilled out my guts—and never heard from him again. And so I figured, fine. I was spending my days at Pixar and having a great time. It was springtime, going into summer. And six years ago a few weeks from now, I got a call back from him [the director], and he said, “We are going to dismiss our CEO, and we would like you to come back and run the company.”

And I said, “I can’t do that. I’m the CEO of Pixar. It’s a publicly traded company. We have all these wonderful employees. We have these shareholders. And I can’t go be CEO of another public … I can’t desert them. So I can’t do this. I’ll help you any way I can, but I can’t.”

He called back a few days later and he said, “We’d like you to come back as an interim leader and help us find a new CEO.”

And I said, “Well, I have to think about that.” And I was thinking about it and called up a friend of mine, a really smart guy, a good friend I’d known for a long time that works at another company in the industry. And I probably woke him up in the morning, about eight o’clock one morning, and I was telling him about my struggles about, should I, could I do this? Should I not? And this and that …

And finally, he interrupted me after about four minutes and he said, “Steve, I don’t give a shit about Apple. Why are you telling me all this?”

And I said, “Oh, OK. I’m sorry.” And I hung up the phone.

And I realized: You know, I do give a shit about Apple.

And that’s kind of what crystallized it for me. And so I went back there as an interim CEO.

And I was terrified because I was afraid our Pixar employees and shareholders would feel like I was deserting them. And that’s why I went back just as an interim CEO. I only planned to stay ninety days. But Apple was in a pretty tough situation, and the candidates it was attracting for the CEO job, they were not so good. And I almost hired one, and at the last minute I just said, “I can’t do this to these guys.”

I just thought, “Well, it will take another ninety days to find somebody.” And that turned into a year. And I decided right up front that I was just going to act like I was the permanent CEO, because they didn’t need a caretaker. This thing was in intensive care. It was about ninety days away from bankruptcy. It was in pretty bad shape.

Email to Apple Employees
“A More Entrepreneurial Apple.”
Steve was not yet CEO when he sent a company-wide email laying out plans to “take Apple back to its roots.”
From: Steve Jobs

To: Apple employees

Subject: A More Entrepreneurial Apple

Date: August 12, 1997, 8:20 a.m.

Renewing Apple is a journey, and we have begun that journey during the past four weeks by taking some decisive first steps—a new Board of Directors, a new product strategy and product roadmap, a decision to really focus on two market segments (education and creative content), a new advertising agency, and a detente and working partnership with Microsoft. Last week we announced some of these steps at MacWorld, and so far our shareholders and the public seem to approve.

Today we are taking a few more steps which will begin to take Apple back to its roots as a more egalitarian, entrepreneurial company. They are:

1. Stock Options - From now on, we will be using stock options as a primary form of “beyond-salary” compensation. Stock options are egalitarian (when anyone’s stock goes up $1 per share, everyone’s stock goes up $1 per share) and they are the best way to give our employees a true stake in the company’s future success. And, we want our employees to be rewarded by the company’s success in the same way that our public shareholders are: through stock appreciation. To lead the way, the Executive Team has agreed to forfeit their current and future cash bonus plans in exchange for more stock options.

As you know, we repriced all stock options to $13.25 on July 11th. In addition, I am pleased to announce that on August 5th our Board approved new stock option grants totaling six million shares at the price of $19.75. Those receiving these new grants will get the good news later this week.

Apple has granted stock options for over 10 million shares since the beginning of this calendar year, and employees now hold stock options for over 20 million shares - which is more than 16% of Apple’s total outstanding shares. This is a very high percentage for a company of Apple’s size, and comparable to many valley start-ups. As we restore Apple’s fortunes, our public shareholders and our employee stock option holders will all benefit in harmony.

2. New Severance Plan - Effective today, we are changing our severance plan for all employees to be more in line with an entrepreneurial company. There will now be only one severance plan for all employees. This plan, like the previous plans, will provide a 60 day notice period, with full pay and benefits. In addition, employees will be eligible to receive one additional week of severance pay for each full year of service. For example, if you have worked at the company for more than three but less than four years, you will receive your pay and benefits during the 60 day notice period plus severance payments equal to three weeks of pay. This new severance plan applies to all employees of Apple, Claris, and Newton in the US - there is no longer a separate executive severance plan.

We will be changing our international severance policies to be in line with this new plan to the extent permitted under local laws.

3. Sabbatical Program - Apple needs all hands on deck for the foreseeable future as we turn our company’s fortunes around. We are therefore discontinuing the sabbatical program at the end of our current fiscal year. Employees who have earned their sabbatical as of September 26, 1997, will be eligible to take their sabbatical at a mutually agreeable time during fiscal year 1998. This applies to all employees of Apple, Claris, and Newton worldwide.

4. Corporate Travel - Corporate travel will continue to be constrained to essential trips. Our egalitarian travel policy specifies coach class travel for everyone on trips lasting less than 10 hours, and business class travel for everyone on trips of 10 hours or longer. Of course individuals may use their personal funds or mileage awards to upgrade their seating class. For clarification, flights between San Francisco and Tokyo (either direction) are eligible for business class travel.

5. Facilities - We will continue to move as many employees as possible onto our R&D Campus site. We will greatly benefit by the resulting “beehive” effects, including faster communication paths and more unplanned interactions between the various groups. Reflecting this consolidation, we are renaming the R&D Campus to the Apple Campus, beginning today.

Thank you for your support as we work together to renew Apple.

Steve and the Executive Team

Speech to Apple Employees
“We believe that people with passion can change the world for the better.”
Steve introduced the “Think Different” advertising campaign to a small group of Apple employees on September 23, 1997. The ad would go on to win an Emmy Award for Outstanding Commercial.
Howdy. Good morning. We were up till three o’clock last night finishing this advertising, and I want to show it to you in a minute—see what you think of it.

I’ve been back about eight to ten weeks, and we’ve been working really hard. What we’re trying to do is not something really highfalutin. We’re trying to get back to the basics. We’re trying to get back to the basics of great products, great marketing, and great distribution. I think that Apple has pockets of greatness but in some ways has drifted away from doing the basics really well.

We started with the product line. We looked at the product road map, going out for a few years, and we said, “A lot of this doesn’t make sense, and it’s way too much stuff, and there’s not enough focus.” We actually got rid of 70 percent of the stuff on the product road map. I couldn’t even figure out the damn product line after a few weeks. I kept saying, “What is this model? How does this fit?”

I started talking to customers, and they couldn’t figure it out either.

You’re going to see the product line get much simpler, and you’re going to see the product line get much better. There’s some new stuff coming out that’s incredibly nice. In addition, we’ve been able to focus a lot more on the 30 percent of the gems and add some new stuff in that is going to take us in some whole new directions. So we are incredibly excited about the products. I think we’re really thinking differently about the kinds of products we have to build. The engineering team is incredibly excited. I mean, I came out of the meeting with people that had just gotten their projects canceled, and they were three feet off the ground with excitement ’cause they finally understood where in the heck we were going, and they were really excited about the strategy.

In the same way we, I think, have not been as … we have not kept up with innovations in our distribution. I’ll give you an example. I’m sure it was talked about this morning, but we’ve got anywhere from two to three months of inventory in our manufacturing supplier pipeline, and about an equal amount in our distribution channel pipeline. We’re having to make guesses four or five, six months in advance, about what the customer wants.

We’re not smart enough to do that. I don’t think Einstein’s smart enough to do that. So what we’re going to do is get really simple and start taking inventory out of those pipelines so we can let the customer tell us what they want, and we can respond to it super fast. You’re going to see us be doing a lot of things like that. Today is just the first of many things we’re going to be doing with you.

We’re going to be not only, I think, catching up to where the best of the best are in distribution, but we’re going to actually be innovating and be breaking some new ground, I think, in the coming several months. I’m pretty excited about that as well, in the distribution manufacturing side of things.

That gets us to the marketing side of things.

To me, marketing is about values. This is a very complicated world. It’s a very noisy world, and we’re not gonna get a chance to get people to remember much about us. No company is.

And so we have to be really clear on what we want them to know about us. Now, Apple, fortunately, is one of the half-a-dozen best brands in the whole world—right up there with Nike, Disney, Coke, Sony. It is one of the greats of the greats, not just in this country but all around the globe.

But even a great brand needs investment and caring if it’s going to retain its relevance and vitality. And the Apple brand has clearly suffered from neglect in this area in the last few years. And we need to bring it back. The way to do that is not to talk about speeds and feeds. It’s not to talk about MIPS and megahertz. It’s not to talk about why we are better than Windows. The dairy industry tried for twenty years to convince you that milk was good for you. It’s a lie, but they tried anyway. And the sales were going like this [hand mimics a line running down and to the right]. And then they tried “Got Milk?” and the sales started going like this [hand goes up and to the right]. “Got Milk?” doesn’t even talk about the product! As a matter of fact, the focus is on the absence of the product.

But the best example of all, and one of the greatest jobs of marketing that the universe has ever seen, is Nike. Remember: Nike sells a commodity! They sell shoes! And yet when you think of Nike, you feel something different than a shoe company. In their ads, as you know, they don’t ever talk about the products. They don’t ever tell you about their air soles, and why they are better than Reebok’s air soles. What does Nike do in their advertising? They honor great athletes, and they honor great athletics. That’s who they are. That’s what they are about.

Apple spends a fortune on advertising. You’d never know it. You’d never know it.

So when I got here, Apple had just fired their agency, and there was a competition with twenty-three agencies, and, you know, four years from now, we would pick one. We blew that up, and we hired Chiat/Day, the ad agency I was fortunate enough to work with several years ago. We created some award-winning work, including the commercial voted the best ad ever made, “1984,” by advertising professionals.

We started working about eight weeks ago. The question we asked was, “Our customers want to know: Who is Apple, and what is it that we stand for? Where do we fit in this world?”

And what we’re about isn’t making boxes for people to get their jobs done, although we do that well. We do that better than almost anybody, in some cases.

But Apple is about something more than that. Apple, at the core—its core value—is that we believe that people with passion can change the world for the better. That’s what we believe.

And we’ve had the opportunity to work with people like that. We’ve had the opportunity to work with people like you, with software developers, with customers, who have done it—in some big and some small ways.

And we believe that in this world, people can change it for the better. And that those people that are crazy enough to think that they can change the world are the ones that actually do.

And so, what we’re going to do, in our first brand-marketing campaign in several years, is to get back to that core value. A lot of things have changed. The market is a totally different place than it was a decade ago. And Apple’s totally different, and Apple’s place in it is totally different. And believe me: the products, and the distribution strategy, and manufacturing are totally different—and we understand that. But values and core values: those things shouldn’t change. The things that Apple believed in at its core are the same things that Apple really stands for today. And so we wanted to find a way to communicate this. And what we have is something that I am very moved by. It honors those people who have changed the world. Some of them are living. Some of them are not. But the ones that aren’t, as you’ll see, you know that if they ever used a computer, it would have been a Mac.

And the theme of the campaign is “Think Different.” It’s honoring the people who think different and who move this world forward. It is what we are about. It touches the soul of this company.

So I’m going to go ahead and roll it, and I hope that you feel the same way about it that I do.


Email to Apple Employees
“Newton protest today.”
When Steve returned to Apple, he jettisoned many product lines developed during his time away. His goal was to focus the company’s offerings. Some fans rebelled.
From: Steve Jobs

To: Apple employees

Subject: Newton protest today

Date: March 6, 1998, 8:09 a.m.

Some people are understandably upset that Apple has decided to stop developing future Newton OS based computers, especially the MessagePad. Today some of them are coming to Apple to protest our decision. This is OK. We are reserving a space for them on our campus and will provide them with coffee and other hot drinks (it may be cold out there!).

Our decision to end Newton development was not taken lightly, and is unlikely to be reversed. Even so, let’s welcome the Newton customers and developers who come to protest this decision. Hopefully they will feel our enthusiasm about the future of Apple, and leave more settled than they arrived.

Thanks

Steve


Email from Steve to Himself
“Apple’s Reason For Being.”
Steve often captured his thoughts by emailing himself notes.
From: Steve Jobs

To: Steve Jobs

Subject: Apple’s reason for being

Date: October 29, 2000, 4:39 p.m.

Apple is the world’s premier company at building high technology products that are easy to learn and use by mere mortals. Beginning over 20 years ago, Apple has consistently set the standard for easy to use computer systems and software. Why do we do this? Because we are in love with the potential for personal computers to enhance and enrich the lives of regular people - not just with spreadsheets and databases, but with creative

We’re a creatively driven company in everything we do. From breakthrough product features and operating systems to culturally leading product design and advertising. Heck, we INVENTED the personal computer, spawned desktop publishing and are now bringing desktop movies to millions. And our engineers are hard at work on several more exciting breakthroughs you’ll see in 2001.

Apple marries state of the art technology with Apple’s legendary ease-of-use to create products that enable users to do more

Apple is the world’s premier bridge builder between mere mortals and the exploding world of high technology. Apple enables mere mortals around the world to grasp by making it easy to learn and use

Apple is the premier company in the world at making the exploding world of high technology easy to learn and use, thereby enabling mere mortals to enrich their lives using it.

Demystified technology, it will have a much greater impact than any other thing we can do. The stores need to be thought of as a mecca for understanding technology and making all of the digits a part of your life. All things digital, digital music, digital photography, people who’ve migrated to broadband, people/families who want to build a home network


Speech to Pixar Employees
“Hopefully we captured a bit of Pixar’s soul in this building.”
In November 2000, Steve officially opened Pixar’s headquarters building in Emeryville, California.
I just wanted to say a few words as we sort of come together to live here. You know, I have seen this building, every square millimeter of this building, in almost every stage of its planning and development and construction—except for one thing, which is I have never seen people in it. It makes all the difference. This big space here looks pretty big without people in it, and with all of us in it, it looks just right.

We are moving from Point Richmond, where we have lived for eleven years, to our new home here, where I think we are going to live forever. We have land to expand here, and I think a lot of us will spend the rest of our corporate lives here.

We are moving from four buildings to one. One of the things people have said this morning is they are seeing people for the first time that work at our company. That’s both startling and kind of exciting. We have designed this building to be a more urban environment—that’s what this is, this is Town Square right here—and it’s a place for you to meet people you have never met before, a place for us to interact and collaborate, which is really the basis of our success. So it’s a very different feeling to get us all into one building, and yet provide us a nice park so we can get away from everybody else when we need to.

We bought this land four years ago. It was a giant Del Monte Fruit Cocktail factory. It had been abandoned and was decrepit. It was falling apart, and for some reason, we saw the land underneath it that no one else saw. We bought it. We bought sixteen gorgeous acres of land, which is one of the rare large parcels of land left in the Bay Area.

Deciding what building to build was really hard. When you are in rented buildings, it is easy because they don’t define who you are—they define who the landlord is! But when you decide to design your own building, you have to ask the question, “Who are we?” Because you want to capture some of the soul of the company in the building and reflect who we are.

The design proceeded much like one of our films. First, a treatment; throw it away. Then another; throw it away. And finally, one that is worth developing—and then zillions and zillions of iterations, model after model after model, detail after detail. We drove our architects crazy. And three years of development—again, much like one of our films.

And hopefully we captured a bit of Pixar’s soul in this building. Our architects did an amazing job. This is also a hand‑made building. All the steel is hand-joined on this site and bolted together, not welded. Just the drawings to define every connection for every place where steel is bolted to steel were twenty-five hundred pages. Every brick was custom hand‑made, with an old, not-seen-today process, and then hand-laid on the site. John [Lasseter] even laid a brick—right over there. And every floorboard was hand-laid and sanded on the site. This is a handmade building, just like one of our films.

And the workers discovered that this crazy owner was letting them build a building like they always had dreamed of, like none other built these days. And they brought their families to the construction site on weekends to see their craftwork like no one else is doing today—just like all of us feel about our films. And though a little blood was spilled, no one was seriously hurt building this building, just like one of our films.

This land and building and grounds cost just shy of $100 million, about the same as it costs to make one of our films. This equals around one year’s salary and benefits for everybody in our studio: to build this whole place, to buy the land, to build the grounds. We are making this investment in our future because we want the best place in the world to support the best talent in the world making the best animated features in the world.

And we paid for it in cash. We have no debt on this building. We own it. Basically, this building was paid for with the profits we made from A Bug’s Life. And we still have over $200 million of cash in the bank. This building will be a solid investment, just like one of our films.

Pixar’s home was in Point Richmond for eleven years. Now our home is here, and many of us will spend the remainder of our professional lives here.

We are having an open house and holiday party here on Saturday, December 9, in the afternoon and early evening, when you can bring your family to see our new home. This home has been lovingly built by talented workers; the building has good karma already. But its purpose is not just to be a cool building or to impress anyone on the outside. It is to house and inspire the most talented group of filmmakers in the world—that’s you. And so today, the architects, Tom, Craig, and the amazing crew that we have here at the company, all of the facilities crew and the I.S. [Information Systems] crew, and everybody who has moved us seamlessly over the last week, we are officially turning the building over to you: the creative owners.

So go make some history here!

One More Thing …
Life can be much broader once you discover one simple fact—and that is: everything around you that you call life was made up by people that were no smarter than you.

And you can change it.

You can influence it.

You can build your own things that other people can use.

And the minute you can understand that you can poke life, and if you push in, then something will pop out the other side; that you can change it, you can mold it—that’s maybe the most important thing: to shake off this erroneous notion that life is there, and you’re just going to live in it versus embrace it, change it, improve it, make your mark upon it.

I think that’s very important, and however you learn that, once you learn it, you’ll want to change life and make it better. Because it’s kind of messed up in a lot of ways.

Once you learn that, you’ll never be the same again.

—Steve, 1994


# INPUT

INPUT:
{sys.argv[1]}
"""


def text_stream():
    yield from (chunk.content for chunk in llm.stream(PROMPT))


audio = eleven.generate(
    text=text_stream(),
    voice="Bmp5BEPIYjmAGTAzMPKr",  # JOBS
    model="eleven_multilingual_v2",
    stream=True,
    voice_settings=VoiceSettings(
        use_speaker_boost=True, stability=0.5, similarity_boost=0.5
    ),
)

audio1, audio2 = itertools.tee(audio, 2)
try:
    stream(audio1)
finally:
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    save(audio2, f"audio/jobs-{timestamp}.mp3")
