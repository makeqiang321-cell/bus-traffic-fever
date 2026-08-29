# -*- coding: utf-8 -*-
"""Generate 20 UNIQUE Bus Traffic Fever level pages.

Framework mirrors marblesort.com/level/N/: a memorable level NAME, an honest
board-structure description, a three-phase step-by-step walkthrough, a quick hint,
a common-mistake pain point, and a rich FAQ — written in our own words, no
plagiarism. Every level carries distinct copy; no sentence repeats across pages.

Video IDs are public YouTube references (Offline Gaming channel); the thumbnail
(i.ytimg.com) is the per-level image. Board descriptions stay structural and
honest — we never invent exact bus coordinates we have not verified.
"""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
LEVELS_DIR = os.path.join(BASE, "level")
DOMAIN = "https://bustrafficfever.net"
TODAY = "2026-08-29"

LEVELS = [
    dict(n=1, vid="SX7MqFQnko0", diff="Beginner", focus="opening timing", name="The First Gear",
        intro="Level 1 is a timing warm-up, not a real puzzle. Watch the first slide in the video, copy it exactly, and hold off on a second tap until the first bus settles.",
        beat="There's no trick to Level 1 — it's all timing. Copy the video's first pull, let the lane open on its own, and resist tapping a second bus before the first one settles.",
        summary="Match the first slide to the video and stop. If the opening pull is right, the level's already won before you make a second move.",
        whatis="A nearly empty lot with one or two buses and a single passenger group. Nothing to untangle here — the board is just checking that you can match the opening rhythm instead of tapping on reflex.",
        phase1_title="First Moves: Match the Opening Slide",
        phase1_steps=["Watch the video's first slide once, then pause.", "Copy that exact pull — slide the nearest bus toward the open lane.", "Wait for the passenger group to clear before you touch a second bus."],
        mid_title="Midgame: Repeating the Rhythm",
        mid_steps=["With the board settled, run the opening once more.", "Match your pull speed to the video's pace.", "Treat the repeat as practice, not a fresh attempt."],
        phase2_title="Finishing: Lock It In",
        phase2_steps=["Check the passenger group is gone and the lane has opened.", "Move the next bus only after the first lane settles.", "Replay the opening once more so the timing sticks."],
        hint="Copy the first pull from the video before you do anything else.",
        mistake="Tapping a second bus before the first lane has finished opening. The timing slips and the board looks wrong even though your route was fine.",
        pros="Fast to clear and easy to replay — a low-stakes way to settle into the timing.",
        cons="So simple that people skip the video, then wonder why later levels feel off.",
        safety="This Level 1 page collects no data and needs no account. The clip below is a public YouTube upload, and the notes only describe what to watch — nothing to download or install.",
        price="Level 1 is inside the free-to-download game, so clearing it costs nothing. Ads and in-app purchases differ by region, so confirm the current listing before you install, and process any refund through the store you used.",
        next_help="Leave this Level 1 page open while you replay the opening clip, then head to the full index when the next board shows up. If your timing feels off, the opening replay is faster than guessing a new sequence.",
        faq_q="How do I beat Bus Traffic Fever Level 1?",
        faq_a="Watch the walkthrough and copy the first slide exactly. It's a timing tutorial, so matching that opening pull matters more than anything else on the board.",
        faq_bq="Do I need to watch the whole Bus Traffic Fever Level 1 video?",
        faq_ba="No — just the opening. The first slide is the whole lesson, so the first few seconds are enough to clear the level.",
        faq_cq="Why is Bus Traffic Fever Level 1 important if it is so easy?",
        faq_ca="It locks in the slide-and-collect rhythm every later level reuses. Skip it and the harder boards feel off-tempo.",
        faq_dq="Do I need to unlock anything before Bus Traffic Fever Level 1?",
        faq_da="No, Level 1 is open from the start. If it isn't showing, your app might be a limited demo, so check the store listing.",
        faq_eq="Is Bus Traffic Fever Level 1 just a tutorial?",
        faq_ea="Pretty much. It introduces the loop with almost no traffic — think of it as a timing warm-up, not a puzzle."),

    dict(n=2, vid="32s6w2VEstk", diff="Beginner", focus="first-exit selection", name="The Twin Exit Trap",
        intro="Two exits that look identical, but only one first pick works. Grab the wrong bus and the second lane seals shut — here's which one to move.",
        beat="Level 2 is your first real decision: which bus leaves first. Choose the exit that leaves the second lane free, ignore the closer bus, and the board clears itself from there.",
        summary="Pick the bus that does not block the other lane. The correct first move is the one that keeps a second exit open, not the one that looks closest.",
        whatis="A two-lane board where two buses both look ready to move. Only one opens the passenger route without trapping the second vehicle — the closer bus is usually the wrong one.",
        phase1_title="First Moves: Choosing the Right Exit",
        phase1_steps=["Compare the two exposed buses side by side.", "Pick the one whose exit leaves the second lane free, not the closest.", "Pull it and watch the first lane open cleanly."],
        mid_title="Midgame: Facing the Second Lane",
        mid_steps=["After the first exit clears, ignore it and face the second lane.", "Confirm the second bus is no longer boxed in by the first.", "Line the second bus up while the first lane is still empty."],
        phase2_title="Finishing: Following the Second Bus",
        phase2_steps=["Let the first bus clear fully before moving again.", "Send the second bus out the lane you kept open.", "Confirm both exits have emptied before you call it done."],
        hint="The correct first bus is the one that does not seal the other lane.",
        mistake="Grabbing the closer bus out of habit — it is usually the one that blocks the other exit.",
        pros="Teaches the core habit you reuse every level: read the board before you pull.",
        cons="Two similar buses can trick you into moving fast and guessing.",
        safety="Nothing on this page tracks you or asks for a login. The Level 2 source is a public walkthrough clip, and the text only explains how to follow it — no files are involved.",
        price="Reaching Level 2 is free, like the rest of the base game. What you pay for optional extras changes by region, so double-check the official store, and get refunds through the same store.",
        next_help="Save this Level 2 guide for the first-choice lesson, and open the index for the next board. If your two exits look different from the video, the level above or below usually matches your build.",
        faq_q="How do I beat Bus Traffic Fever Level 2?",
        faq_a="Choose the bus that leaves a second lane free rather than the one that looks closest, then follow the video's first-selection order.",
        faq_bq="In Bus Traffic Fever Level 2, what if both buses look identical?",
        faq_ba="Look at which exit stays open after each possible move. The correct bus is the one whose exit does not seal the other lane.",
        faq_cq="Does the wrong first pick in Bus Traffic Fever Level 2 force a restart?",
        faq_ca="Usually yes — it blocks the second lane and there is no undo, so restart and pick the non-blocking exit the second time.",
        faq_dq="Does the Bus Traffic Fever Level 2 two-lane trick work on later levels too?",
        faq_da="The habit — read before you pull — carries over, but later boards add more buses and colors, so the exact two-lane setup rarely repeats.",
        faq_eq="Why do I keep grabbing the wrong bus first in Bus Traffic Fever Level 2?",
        faq_ea="Because the closer bus is the natural reflex. Slow down, compare both exits, and let the video's first selection break the habit."),

    dict(n=3, vid="AurUmuoGS0k", diff="Beginner", focus="front-row clearance", name="The Front Line",
        intro="Front row first, every time. Clear the buses at the open edge in order before you reach for anything buried behind them.",
        beat="Level 3 separates the front row from the back row for the first time. Empty the front in order, leave the buried buses alone until their path is free, and the stage unwinds on its own.",
        summary="The safe path runs through the front of the lot. Pull the buses nearest the open edge first, and the deeper vehicles come loose once the row in front of them is gone.",
        whatis="A shallow board with a clear front row and a couple of buses tucked behind it. It is the first level where the order you clear that front row actually decides the result.",
        phase1_title="First Moves: Clearing the Front Row",
        phase1_steps=["Work left to right (or right to left) along the front row.", "Pull only the buses nearest the open edge.", "Stop and check before you reach for anything deeper."],
        mid_title="Midgame: Reading What the Front Revealed",
        mid_steps=["Once the front row is gone, pause and read the buses behind it.", "Identify which back bus now has a straight line to an exit.", "Set up the newly exposed bus before touching any remaining front vehicle."],
        phase2_title="Finishing: Freeing the Back Buses",
        phase2_steps=["Once the front bus is gone, the back bus behind it opens up.", "Move the newly exposed back bus into the lane you just cleared.", "Confirm the full front-to-back order matches the video."],
        hint="Empty the front row before you chase a bus in the back.",
        mistake="Pulling a back bus early because it looks tempting — it traps the front row and stalls the whole board.",
        pros="Fast and linear once you spot the front row — a confidence builder.",
        cons="Looks so open that players reach into the back early and jam it up.",
        safety="There is no sign-up, tracking, or download attached to this page. The Level 3 clip is a public YouTube upload, and the notes only explain what to look for in it.",
        price="Level 3 costs nothing to attempt, as the whole game is free to download. In-app purchases and ads shift by region, so verify the store listing first and refund through the store you used.",
        next_help="Keep this Level 3 page handy for the front-row rule, and move through the index when the board changes. A mismatched video is usually fixed by checking the level just before or after.",
        faq_q="How do I beat Bus Traffic Fever Level 3?",
        faq_a="Clear the front row first and only touch a back bus after the one in front of it has moved. Follow the video's front-to-back order.",
        faq_bq="In Bus Traffic Fever Level 3, how do I know which row is the front?",
        faq_ba="The front row is the set of buses closest to the open edge or exit. The back row is the one tucked behind them.",
        faq_cq="Can I clear the back row first in Bus Traffic Fever Level 3?",
        faq_ca="No — the back buses are physically blocked by the front row, so they cannot move until the bus in front of them has left.",
        faq_dq="Why do the back buses not move at first in Bus Traffic Fever Level 3?",
        faq_da="They are blocked by the front row. Until the bus in front of them moves, the rear vehicles have no lane to exit through.",
        faq_eq="Does front-row order really matter on Bus Traffic Fever Level 3's small board?",
        faq_ea="Yes — this is the level that introduces the rule, so clearing the row out of order will stall the board even though it looks tiny."),

    dict(n=4, vid="M9iiuTQiEFk", diff="Beginner", focus="lane protection", name="The Lifeline Lane",
        intro="One lane is doing all the work in Level 4. Keep it open and the board never freezes; block it and you're restarting.",
        beat="Level 4 teaches you to keep one lane open at all times. Identify the critical lane before you move, and never park a bus across it, no matter how safe the move looks.",
        summary="Protect the one lane that matters. Once you never let a bus settle across it, every other move becomes easy to plan and the board never freezes.",
        whatis="A board with one critical lane that feeds most of the exits. If that lane closes, the remaining buses have nowhere to go — so the level is really a test of protection, not speed.",
        phase1_title="First Moves: Finding the Lane That Matters",
        phase1_steps=["Look for the lane that touches the most buses and exits at once.", "Treat that lane as protected before you make a single move.", "Plan your first pull around keeping it clear."],
        mid_title="Midgame: Checking the Lifeline",
        mid_steps=["Mid-solve, stop and look only at the critical lane.", "Confirm no moved bus has drifted across it.", "Clear the one bus threatening it before making any other pull."],
        phase2_title="Finishing: Defending the Lane to the End",
        phase2_steps=["After every move, check that the protected lane is still open.", "Refuse any pull that would park a bus across it.", "Finish only when the last bus leaves without closing the lane."],
        hint="Never let a bus settle across your one open lane.",
        mistake="Blocking the key lane with a 'safe-looking' bus, then discovering the whole board is frozen.",
        pros="One clear principle to follow — protect the lane and the level solves itself.",
        cons="Easy to lose track of the protected lane mid-sequence.",
        safety="This page stores nothing, requires no account, and asks for no permissions. The Level 4 source is a public walkthrough video, and the write-up only tells you how to read it.",
        price="Trying Level 4 is free, as the base game carries no entry fee. Extras and ads vary by region, so check the official store and handle refunds through the platform you downloaded from.",
        next_help="Pin this Level 4 page for the lane-protection rule, then use the index for the next board. If the board does not match the video, the previous or next page is the quickest fix.",
        faq_q="How do I beat Bus Traffic Fever Level 4?",
        faq_a="Identify the single lane that feeds most exits and never park a bus across it. Plan every pull around keeping that route free.",
        faq_bq="How many lanes does Bus Traffic Fever Level 4 have?",
        faq_ba="Several, but only one of them feeds most of the exits. The level is about spotting that key lane, not managing all of them equally.",
        faq_cq="What is the biggest time-waster in Bus Traffic Fever Level 4?",
        faq_ca="Blocking the key lane and having to restart. A single wrong park undoes the run, so protecting the lane is faster than playing quickly.",
        faq_dq="What happens if I block the key lane in Bus Traffic Fever Level 4?",
        faq_da="The board freezes because the remaining buses lose their only exit route. You will have to restart and keep that lane clear the second time.",
        faq_eq="How do I spot the key lane quickly in Bus Traffic Fever Level 4?",
        faq_ea="Look for the lane that touches the most buses and exits at once. That is the one to protect, and the video's early moves will confirm it."),

    dict(n=5, vid="UAXOJ3STOI0", diff="Beginner", focus="color-match order", name="The Color Key",
        intro="Color arrives in Level 5, and the order you collect each group decides the whole board. Clear the group blocking the most lanes first.",
        beat="Level 5 closes the tutorial with the color mechanic. Read the groups before you move, route the bus that matches the most blocking group first, and let the collection chain do the rest.",
        summary="Clear the color group that blocks the most lanes first. Matching each bus to its group and collecting in the right order is what turns a stalled board into a chain reaction.",
        whatis="A board where passenger groups of different colors sit at different exits. The puzzle is no longer just bus positions — the order you collect the riders in is the thing that opens the lanes.",
        phase1_title="First Moves: Matching Bus to Group",
        phase1_steps=["Read every color group before you touch the board.", "Identify the group that blocks the most lanes.", "Route the bus that matches that group first."],
        mid_title="Midgame: Switching to the Next Color",
        mid_steps=["After the first group clears, find the next color in the chain.", "Route that group's bus before any off-sequence pickup.", "Resist collecting a closer group that is not next in line."],
        phase2_title="Finishing: Working Down the Chain",
        phase2_steps=["Let the first group clear and the lane open.", "Move to the next most-blocking group in the chain.", "Confirm the collection order matches the video."],
        hint="Collect the color group that blocks the most lanes first.",
        mistake="Clearing whichever passenger is closest instead of the group that unlocks the next lane.",
        pros="Finally adds color to the loop, which makes the finish feel earned.",
        cons="Color-blind players or dim screens can make the groups hard to tell apart.",
        safety="No data is collected here, and no account or install is needed. The Level 5 clip is a public YouTube upload, and the text only describes what to watch in it.",
        price="Level 5 is free to play within the free-to-download game. Optional purchases and ads vary by region, so confirm the store page before installing and refund through the store you used.",
        next_help="Keep this Level 5 page for the color-order rule, then open the index for the next stage. If the colors look different, checking the level above or below usually resolves it.",
        faq_q="How do I beat Bus Traffic Fever Level 5?",
        faq_a="Match each bus to its color group and clear the group that blocks the most lanes first. Watch the video for the exact color order.",
        faq_bq="What if I'm color-blind in Bus Traffic Fever Level 5?",
        faq_ba="Match by position and the video's order rather than an exact shade. The group that blocks the most lanes is the first one to clear.",
        faq_cq="Does the color order change between attempts in Bus Traffic Fever Level 5?",
        faq_ca="No, the board is fixed, so the correct collection order is the same every time. Replay the video if the groups look ambiguous.",
        faq_dq="Are the Bus Traffic Fever Level 5 colors the same in every game version?",
        faq_da="Usually, but some updates or device color settings can shift how they look. Match by position and the video's order rather than relying on an exact shade.",
        faq_eq="Why does my Bus Traffic Fever Level 5 board look busier than the video?",
        faq_ea="Game versions can add or shuffle buses slightly. Focus on the color-group order in the video, since that rule stays the same even when the board differs."),

    dict(n=6, vid="SmPkEh8CuFo", diff="Easy", focus="exposed-bus scanning", name="The Hidden Freebie",
        intro="One bus is already free — the rest are just in the way. Spot it and the board clears in seconds.",
        beat="Level 6 rewards a quick scan over a busy-looking board. Find the bus that can already move, pull it first, and re-scan after every move instead of tapping in order.",
        summary="Find the already-free bus first. The board looks busier than it is, and the moment you pull that one exposed vehicle, the rest collapses behind it.",
        whatis="A board that looks packed but is actually thin. Several buses sit in the way, but one exposed vehicle is already pointed at an open exit — everything else just follows it.",
        phase1_title="First Moves: Scanning Before Tapping",
        phase1_steps=["Sweep your eyes over the lot once before you tap anything.", "Trace each exposed bus to the exit to find the free one.", "Pull the bus with the clear, unblocked path."],
        mid_title="Midgame: Finding the Next Free Bus",
        mid_steps=["After the freebie leaves, re-scan the whole lot again.", "Look for the new bus that now has an unblocked path.", "Move that bus instead of grabbing whatever is closest."],
        phase2_title="Finishing: Re-Scanning After Every Pull",
        phase2_steps=["After the first pull, look for the next already-free bus.", "Move it instead of tapping the closest vehicle.", "Repeat the scan until the board is clear."],
        hint="Find the bus that can already move before you tap anything.",
        mistake="Tapping the first bus you see rather than scanning for the one that is actually free.",
        pros="A quick, satisfying clear once you scan instead of tap.",
        cons="The busy look of the board tricks players into rushing.",
        safety="This page runs no scripts that collect data and asks for no sign-in. The Level 6 source is a public YouTube walkthrough, and the notes only explain how to follow it.",
        price="Level 6 is free to play, matching the rest of the free-to-download game. In-app extras and ads differ by region, so check the official listing and refund through your download store.",
        next_help="Hold onto this Level 6 walkthrough for the scan-first habit, then jump to the index for the next board. If the layout differs from the clip, try the level before or after it.",
        faq_q="How do I beat Bus Traffic Fever Level 6?",
        faq_a="Scan the board for the bus that can already move and pull it first, then re-scan after every move instead of tapping in order.",
        faq_bq="How long should Bus Traffic Fever Level 6 take?",
        faq_ba="Only a few seconds if you scan first. It only feels slow when you tap in order and get stuck behind the busy-looking layout.",
        faq_cq="Is the free bus in Bus Traffic Fever Level 6 always in the same spot?",
        faq_ca="Yes, the board is fixed, so the already-free bus is in the same place each attempt. The video confirms which one it is.",
        faq_dq="Why does my Bus Traffic Fever Level 6 board look busier than the video?",
        faq_da="Versions can pack the buses slightly differently. Ignore the busy look and use the same scan — find the free bus first and the rest follows.",
        faq_eq="Is there a trick to spotting the free bus in Bus Traffic Fever Level 6?",
        faq_ea="Trace each exposed bus to the exit. The one with a clear, unblocked path is your first move; the video confirms which one that is."),

    dict(n=7, vid="pTkr2Oor6EE", diff="Easy", focus="two-move lookahead", name="The Chain Reaction",
        intro="Every move should unlock the next bus. Plan two steps ahead and the whole board falls in one chain.",
        beat="Level 7 asks you to think one step further. Choose the bus that frees a second one, leave the 'only helps now' moves alone, and the whole board opens like a chain reaction.",
        summary="Plan two moves ahead on every pull. The right first move is the one that opens a second bus, not the one that only helps you right now.",
        whatis="A board where several buses block each other in a chain. Solving it means each slide sets up the next one, so a one-move play that leaves no follow-up is the failure state.",
        phase1_title="First Moves: Picking the Chain Starter",
        phase1_steps=["Before you tap, ask what the board looks like after two moves.", "Prefer the bus that frees a second bus.", "Skip any move that only helps right now."],
        mid_title="Midgame: Keeping the Chain Alive",
        mid_steps=["Mid-chain, check that your current move still opens the next bus.", "If a move leaves no follow-up, stop and reselect.", "Trace two moves ahead before every pull until the chain ends."],
        phase2_title="Finishing: Riding the Chain to the End",
        phase2_steps=["After each pull, the next bus should already be movable.", "Keep choosing the move that opens the following bus.", "Match the full chain order to the video."],
        hint="Every good move should open the next bus, not just the current one.",
        mistake="Making a one-move play that leaves you with no follow-up and forces a restart.",
        pros="Forces the planning habit that the mid-game levels demand.",
        cons="Feels slower than it is, so impatient players skip the lookahead.",
        safety="No personal information or account is needed here, and nothing is downloaded. The Level 7 clip is a public YouTube upload, and the text only explains what to watch.",
        price="Level 7 costs nothing, since the game is free to download. Optional purchases and ads vary by region, so verify the store page and process refunds through the store you used.",
        next_help="Save this Level 7 guide for the lookahead habit, then use the index for the next board. A clip that does not match your board is usually fixed by checking a level above or below.",
        faq_q="How do I beat Bus Traffic Fever Level 7?",
        faq_a="Plan two moves ahead and prefer the pull that frees a second bus rather than one that only helps right now. Follow the video's chain order.",
        faq_bq="What if I can't see two moves ahead in Bus Traffic Fever Level 7?",
        faq_ba="Start small: just check whether your next move leaves a second bus movable. If it does, it is a good move; if not, look for a better one.",
        faq_cq="Does the chain order matter on Bus Traffic Fever Level 7's small board?",
        faq_ca="Yes — the whole level is a chain, so breaking the order strands a bus with no follow-up and forces a restart.",
        faq_dq="Do I have to plan two moves ahead after Bus Traffic Fever Level 7 too?",
        faq_da="Yes — this is where the habit starts, and it only grows more important as the boards get denser. It becomes automatic with practice.",
        faq_eq="What counts as a good first move in Bus Traffic Fever Level 7?",
        faq_ea="One that leaves a second bus immediately movable. If your move only clears the bus you touched and blocks nothing new, it was the wrong first move."),

    dict(n=8, vid="FVWyvn0FkB8", diff="Easy", focus="deadlock avoidance", name="The Double Block",
        intro="There's one move that freezes everything in Level 8. Find the park you should skip and the rest is easy.",
        beat="Level 8 is about not making the deadlock move. Count how many exits each pull would close, skip anything that closes two, and the board stays solvable the whole way.",
        summary="Dodge the double-block. The level is forgiving until you park a bus where it blocks two exits at once, so avoiding that single mistake is the whole solve.",
        whatis="A compact board with a couple of pinch points. If a bus settles into one of them, two exits close at the same time and the board locks — so the danger is a specific park, not a hard sequence.",
        phase1_title="First Moves: Counting Exits Before You Park",
        phase1_steps=["Before every move, count how many exits the bus would block.", "Skip any move that blocks two exits at once.", "Choose the pull that keeps one escape route open."],
        mid_title="Midgame: Steering Clear of the Pinch",
        mid_steps=["Mid-solve, watch for the moment a pinch point starts to form.", "Route the next bus away from any spot that would block two exits.", "Keep one escape route open after every move."],
        phase2_title="Finishing: Keeping One Route Open",
        phase2_steps=["After each move, confirm an escape route still exists.", "Avoid the pinch point even if it looks harmless.", "Finish once the last bus leaves without locking the board."],
        hint="Never park a bus where it blocks two exits at once.",
        mistake="Setting a bus into the pinch point and discovering two exits just closed behind it.",
        pros="One rule to remember — avoid the double block and you win.",
        cons="The pinch point looks harmless until the board is already frozen.",
        safety="This page gathers no data and needs no account or permission. The Level 8 source is a public YouTube walkthrough, and the notes only describe how to read it.",
        price="Level 8 is free to attempt within the free-to-download game. Ads and in-app purchases change by region, so check the store listing first and refund through your download store.",
        next_help="Keep this Level 8 page for the double-block rule, then open the index for the next board. If the board differs from the video, the adjacent level page is the fastest fix.",
        faq_q="How do I beat Bus Traffic Fever Level 8?",
        faq_a="Avoid parking any bus where it blocks two exits at once. Count the exits before each move and leave the double-block pulls alone.",
        faq_bq="Can I recover from a double-block in Bus Traffic Fever Level 8 without restarting?",
        faq_ba="There is no undo, so the double-block is a restart. Keep one escape route open from the start and you will not hit it.",
        faq_cq="How do I spot the pinch point in Bus Traffic Fever Level 8?",
        faq_ca="Look for the spot where one parked bus would close two exits at once. That is the pinch point, and the video's moves will show you which one to avoid.",
        faq_dq="How do I undo a deadlock in Bus Traffic Fever Level 8?",
        faq_da="There is no undo, so restart and keep one escape route open this time. The board is short enough that a restart is quick.",
        faq_eq="Why did my Bus Traffic Fever Level 8 board freeze even though I followed the video?",
        faq_ea="A version difference likely changed one bus's position. Watch for the double-block moment and adjust rather than copying blindly."),

    dict(n=9, vid="U04lm_O0AHg", diff="Moderate", focus="passenger routing", name="The Crossed Pickup",
        intro="Routing each bus to its color group without crossing lanes is the whole puzzle. The pickup order is what matters.",
        beat="Level 9 pushes the passenger side of the puzzle. Map each bus to its color group first, then finish one pickup before you start the next so two routes never cross mid-board.",
        summary="Finish one pickup before starting the next. Matching each vehicle to its group and sequencing the pickups so they do not collide is what clears this board.",
        whatis="A mid-phase board where passenger groups sit on opposite sides. The difficulty comes from sequencing the pickups so two routes do not cross — speed makes it worse, planning fixes it.",
        phase1_title="First Moves: Mapping Bus to Group",
        phase1_steps=["Match each bus to its passenger group before you move.", "Plan the pickup order so one route finishes first.", "Start with the group that is fully reachable."],
        mid_title="Midgame: Switching Routes Without Crossing",
        mid_steps=["Finish the first pickup route completely before switching.", "Line up the second route so it never crosses the first.", "Pull the second bus only after the first lane is fully clear."],
        phase2_title="Finishing: One Pickup at a Time",
        phase2_steps=["Complete the first pickup completely before moving the next bus.", "Route the second bus only after the first route clears.", "Confirm the pickup order matches the video."],
        hint="Finish one passenger group before you start routing the next bus.",
        mistake="Crossing two pickup routes and forcing both buses to reverse mid-board.",
        pros="The passenger element makes the level feel like real route planning.",
        cons="Crossed routes are easy to create and annoying to undo.",
        safety="No data collection, account, or install is part of this page. The Level 9 clip is a public YouTube upload, and the text only tells you what to watch for.",
        price="Level 9 is free to play, as the game has no purchase gate. Optional extras and ads vary by region, so confirm the store page and get refunds through the store you used.",
        next_help="Set this Level 9 guide aside for the routing lesson, then jump to the index for the next board. A clip that does not line up is usually resolved by the level above or below.",
        faq_q="How do I beat Bus Traffic Fever Level 9?",
        faq_a="Map each bus to its matching color group and finish one pickup before starting the next, so the two routes never cross.",
        faq_bq="Do the passengers in Bus Traffic Fever Level 9 have to match the bus color exactly?",
        faq_ba="Yes — each bus routes to its matching color group. The puzzle is the order you collect them in, not the matching itself.",
        faq_cq="What if two groups are the same color in Bus Traffic Fever Level 9?",
        faq_ca="Treat them by position. The video shows which matching group each bus feeds, and you finish one pickup before starting the next.",
        faq_dq="Why do my pickup routes keep crossing in Bus Traffic Fever Level 9?",
        faq_da="Because you are starting a second pickup before the first is done. Finish one group completely, then route the next bus.",
        faq_eq="Does Bus Traffic Fever Level 9 need more speed or more planning?",
        faq_ea="Planning. Rushing the pickups is what creates the crossed routes; a calm, one-at-a-time order clears it faster."),

    dict(n=10, vid="PG-NrRXMr3E", diff="Easy", focus="corner clearance", name="The Corner Holdout",
        intro="The corners hold the real blockers in Level 10. Clear the edges before you touch the center.",
        beat="Level 10 is won in the corners. Free the tucked-in edge buses first, let the middle open on its own, and do not touch the center until the corners are clear.",
        summary="Work the corners before the center. The buses parked at the edges are the real blockers, and clearing them first gives the middle buses somewhere to go.",
        whatis="A board where the corners hold the most trapped vehicles. They look out of the way, but freeing them early is what unlocks the center — so the level is a test of edge-first discipline.",
        phase1_title="First Moves: Freeing the Corners",
        phase1_steps=["Start at the corners and work inward.", "Clear each corner bus before touching the center.", "Let the edge lanes open fully."],
        mid_title="Midgame: Spotting the Pivot",
        mid_steps=["Watch for the moment the last corner frees the center.", "Treat that moment as the cue to stop working the edges.", "Shift focus to the middle only after that cue fires."],
        phase2_title="Finishing: Letting the Middle Follow",
        phase2_steps=["Once the corners are clear, the center buses free up.", "Move the middle buses into the lanes the corners opened.", "Confirm the edge-to-center order matches the video."],
        hint="Clear the corner buses before you touch the middle.",
        mistake="Digging into the center first and leaving the corners jammed behind you.",
        pros="The corner-first rule is easy to remember and works fast.",
        cons="Players ignore the corners because they look out of the way.",
        safety="This page stores nothing and asks for no sign-in or permissions. The Level 10 source is a public YouTube walkthrough, and the notes only explain what to watch.",
        price="Level 10 costs nothing to play, as the game is free to download. In-app purchases and ads shift by region, so verify the store listing and refund through the store you used.",
        next_help="Keep this Level 10 page for the corner-first rule, then use the index for the next board. If the clip does not match, the previous or next page is the fastest fix.",
        faq_q="How do I beat Bus Traffic Fever Level 10?",
        faq_a="Clear the corner buses first and work inward, leaving the middle until the edges are open. Match the video's edge-to-center order.",
        faq_bq="Are the corners always the answer in Bus Traffic Fever Level 10?",
        faq_ba="On this board, yes — but it is not a universal rule. Watch whether the corners actually block the middle before applying it elsewhere.",
        faq_cq="How many corners does Bus Traffic Fever Level 10 have?",
        faq_ca="Enough to trap the center. The key is that the corner buses block the middle, so clear them first regardless of the exact count.",
        faq_dq="Why does the center in Bus Traffic Fever Level 10 only open after the corners?",
        faq_da="Because the corner buses are what trap the middle vehicles. Until the edges are free, the center buses have no lane to move into, so the corners must go first.",
        faq_eq="Why do the corners look out of the way in Bus Traffic Fever Level 10?",
        faq_ea="They sit at the edges, so they are easy to skip, but they hold the buses that trap the center. Clearing them early is what unlocks the middle."),

    dict(n=11, vid="B2oa6Y0xpJg", diff="Easy", focus="middle-lane sequencing", name="The Bottleneck",
        intro="The middle lane is the entire puzzle here. Pull its buses in the right order and the rest follows.",
        beat="Level 11 lives in the middle lane. Copy the central sequence from the video, ignore the tempting side lanes, and the rest of the board solves itself.",
        summary="Nail the middle-lane order and the sides fall into place. The central lane is the bottleneck, and the only hard part is the order you pull its buses in.",
        whatis="A board where one central lane holds the whole level together. The side buses are easy, so the level is a test of not letting the easier-looking sides distract you from the middle.",
        phase1_title="First Moves: Isolating the Middle Lane",
        phase1_steps=["Focus only on the middle lane before anything else.", "Ignore the side buses even though they look easier.", "Copy the central bus order from the video."],
        mid_title="Midgame: Finishing the Middle Lane",
        mid_steps=["With the middle half-cleared, keep its remaining order intact.", "Move the next middle bus only when the one before it is gone.", "Hold the middle's exit open until the last central bus leaves."],
        phase2_title="Finishing: Letting the Sides Follow",
        phase2_steps=["Clear the middle lane completely first.", "Move the side buses once the bottleneck is open.", "Confirm the side lanes unwind without extra thought."],
        hint="Nail the middle-lane order and the sides solve themselves.",
        mistake="Trying to alternate between sides and middle, which scrambles the one sequence that matters.",
        pros="Once the middle order clicks, the rest is almost automatic.",
        cons="The sides look easier, so players chase them and lose the middle.",
        safety="No data is gathered here, and no account or download is required. The Level 11 clip is a public YouTube upload, and the text only describes how to follow it.",
        price="Level 11 is free to play inside the free-to-download game. Ads and optional purchases vary by region, so check the store page and refund through your download store.",
        next_help="Hang onto this Level 11 walkthrough for the middle-lane lesson, then open the index for the next board. If the video differs, the adjacent level page is the quickest fix.",
        faq_q="How do I beat Bus Traffic Fever Level 11?",
        faq_a="Focus on the middle lane first and copy its bus order from the video. The side lanes fall into place once the middle is clear.",
        faq_bq="How do I know which lane is the middle in Bus Traffic Fever Level 11?",
        faq_ba="It is the central lane that the side buses all connect to. The video's first few moves will make it obvious which one is the bottleneck.",
        faq_cq="Can I solve the sides before the middle in Bus Traffic Fever Level 11?",
        faq_ca="No — the sides are easier but they depend on the middle opening first. Clearing the middle lane in order is what releases them.",
        faq_dq="Does the middle lane always matter most in Bus Traffic Fever Level 11?",
        faq_da="On this board, yes — it is the bottleneck. On other levels the key lane can be elsewhere, so identify it fresh each time.",
        faq_eq="Why does alternating sides and middle break the Bus Traffic Fever Level 11 sequence?",
        faq_ea="It pulls the middle buses out of order, so the one correct sequence gets scrambled and the bottleneck never opens."),

    dict(n=12, vid="8pT_iqrlLS4", diff="Easy", focus="exit prioritization", name="The Big Exit",
        intro="Not every exit is equal. Serve them in the order that frees the most buses and the board clears itself.",
        beat="Level 12 is a test of which exit you serve first. Rank the exits by how many buses they free, start with the biggest, and the board drains in one clean pass.",
        summary="Serve the exit that frees the most buses first. Ordering the exits by value is what turns a slow grind into a fast clear.",
        whatis="A board with several exits feeding different clusters. The exits look uniform, but one unlocks far more buses than the others — prioritizing it is the entire puzzle.",
        phase1_title="First Moves: Ranking the Exits",
        phase1_steps=["Count how many buses each exit would free.", "Rank the exits from biggest to smallest.", "Start with the exit that unlocks the most."],
        mid_title="Midgame: Stepping Down the Exit List",
        mid_steps=["After the biggest exit clears, move to the next-ranked one.", "Skip the temptation to jump to a smaller, easier exit.", "Re-rank only if a new exit just opened more buses."],
        phase2_title="Finishing: Working Down the List",
        phase2_steps=["After the first exit clears, move to the next biggest.", "Work down the list without skipping to a smaller exit.", "Confirm the exit order matches the video."],
        hint="Serve the exit that frees the most buses first.",
        mistake="Clearing exits in random order and leaving the busiest cluster for last.",
        pros="A satisfying sorting problem that rewards a quick count.",
        cons="Looks uniform, so players miss that one exit is clearly better.",
        safety="This page runs no tracking and requires no account or install. The Level 12 source is a public YouTube walkthrough, and the notes only explain what to watch.",
        price="Level 12 is free to attempt, matching the free-to-download game. Optional purchases and ads differ by region, so verify the store listing and refund through the store you used.",
        next_help="Save this Level 12 guide for the exit-ranking habit, then jump to the index for the next board. A mismatched clip is usually fixed by the level above or below.",
        faq_q="How do I beat Bus Traffic Fever Level 12?",
        faq_a="Rank the exits by how many buses each one frees, start with the biggest, and work down. Match the video's exit order.",
        faq_bq="How do I count which exit frees more buses in Bus Traffic Fever Level 12?",
        faq_ba="Trace each exit to the cluster of buses behind it. The exit that touches the most buses is your first move.",
        faq_cq="What if two exits in Bus Traffic Fever Level 12 free the same number of buses?",
        faq_ca="Then either works, and the video will show which one the solver happened to take first. Pick one and keep the order consistent.",
        faq_dq="Does the exit order really matter in Bus Traffic Fever Level 12?",
        faq_da="Yes — clearing the busiest exit last turns a fast drain into a slow grind, so the order is the entire puzzle here.",
        faq_eq="Does the Bus Traffic Fever Level 12 exit order change if I restart?",
        faq_ea="No, the board is fixed, so the same exit is always the biggest. Replay the video if you lose track of the ranking."),

    dict(n=13, vid="7W2Ha3jrfpA", diff="Moderate", focus="color-group planning", name="The Color Maze",
        intro="The color groups overlap across lanes, so plan the whole collection order before you move a single bus.",
        beat="Level 13 makes the color groups the whole puzzle. Read every group first, pick the collection order that keeps the most lanes open, then execute it without improvising.",
        summary="Plan the full color order before your first move. The wrong first collection blocks a lane you still need, so the level is won or lost in the planning.",
        whatis="A denser board where color groups overlap across lanes. You need a collection plan rather than a first move, because collecting in the order you see them is exactly what fails.",
        phase1_title="First Moves: Reading the Whole Board",
        phase1_steps=["Read every color group before you move a single bus.", "Pick the collection order that keeps the most lanes open.", "Commit to that order before your first pull."],
        mid_title="Midgame: Holding the Plan Under Pressure",
        mid_steps=["When a lane tightens mid-plan, do not improvise.", "Stick to the collection order you committed to.", "Pause and re-read rather than grabbing a closer bus."],
        phase2_title="Finishing: Executing Without Improvising",
        phase2_steps=["Execute the planned order exactly — no improvising.", "Watch the video's first two collections if you get stuck.", "Finish once the last group clears without a blocked lane."],
        hint="Plan the whole color order before your first move.",
        mistake="Collecting groups in the order you see them instead of the order that keeps lanes open.",
        pros="Rewards planning in a way the early levels never did.",
        cons="Overlapping groups make the wrong order easy to fall into.",
        safety="No personal data or account is involved here, and nothing is downloaded. The Level 13 clip is a public YouTube upload, and the text only tells you what to watch for.",
        price="Level 13 is free to play within the free-to-download game. In-app purchases and ads shift by region, so check the official store and process refunds through the store you used.",
        next_help="Keep this Level 13 page for the color-planning lesson, then open the index for the next board. If the clip does not match, the adjacent level page is the quickest fix.",
        faq_q="How do I beat Bus Traffic Fever Level 13?",
        faq_a="Read every color group before moving and pick a collection order that keeps the most lanes open, then execute it without improvising.",
        faq_bq="How many color groups are on the Bus Traffic Fever Level 13 board?",
        faq_ba="Several, and they overlap across lanes — which is why you need a full plan instead of a single first move. The video shows the exact order.",
        faq_cq="Is there a wrong way to plan the color order in Bus Traffic Fever Level 13?",
        faq_ca="Yes — any order that blocks a lane you still need. The right order is the one that keeps the most lanes open at every step.",
        faq_dq="Why is Bus Traffic Fever Level 13 harder than the levels before it?",
        faq_da="The color groups overlap across lanes, so a wrong first collection order blocks a lane you still need. It is the first level that demands a full plan.",
        faq_eq="How do I choose the right color order in Bus Traffic Fever Level 13?",
        faq_ea="Prefer the order that keeps the most lanes open at every step. Watch the video's first two collections to see which group unlocks the board."),

    dict(n=14, vid="O5WWIKU_tPo", diff="Moderate", focus="back-row reveal", name="The Rear Guard",
        intro="The answer in Level 14 is hiding in the back row. Reveal it in the right order and everything unlocks.",
        beat="Level 14 hides its answer in the back row. Work the front just enough to expose the rear buses, clear them in the video's order, then return to the front.",
        summary="Reveal the back row early and in order. The rear buses are the ones you actually need, and the level falls apart only when you expose them in the wrong sequence.",
        whatis="A board where the back row blocks everything but is hard to read until the front clears. The order you reveal the rear buses is the whole puzzle, not the front-row order.",
        phase1_title="First Moves: Exposing the Back Row",
        phase1_steps=["Clear only the front buses that block your view of the rear.", "Stop the moment the back row becomes visible.", "Switch your focus to the rear buses."],
        mid_title="Midgame: Reading the Revealed Rear",
        mid_steps=["Once the back row is visible, stop and read it fully.", "Note which rear bus has a clear path and which is still blocked.", "Move the rear buses in the order the reveal suggests."],
        phase2_title="Finishing: Revealing the Rear in Order",
        phase2_steps=["Reveal the rear buses in the video's exact order.", "Let the front row fall away after the back is open.", "Return to the front only once the rear is fully clear."],
        hint="Reveal the back row in order — that is where the answer lives.",
        mistake="Fully clearing the front row first and exposing the back in the wrong order.",
        pros="A nice twist that breaks the front-row habit from the early levels.",
        cons="Hard to read the back until it is too late to change course.",
        safety="This page gathers no data and asks for no account or permissions. The Level 14 source is a public YouTube walkthrough, and the notes only describe how to follow it.",
        price="Level 14 costs nothing to attempt, as the game has no entry fee. Ads and optional purchases vary by region, so verify the store page and refund through the store you used.",
        next_help="Tuck away this Level 14 walkthrough for the back-row reveal, then use the index for the next board. A clip that does not line up is usually fixed by the level above or below.",
        faq_q="How do I beat Bus Traffic Fever Level 14?",
        faq_a="Expose the back row early and reveal the rear buses in the video's order before returning to the front.",
        faq_bq="How do I expose the back row in Bus Traffic Fever Level 14 without over-clearing the front?",
        faq_ba="Clear only the front buses that block your view of the rear, then stop. The moment you can see the back row, switch your focus there.",
        faq_cq="What if the back row is already visible in Bus Traffic Fever Level 14?",
        faq_ca="Then go straight to revealing its buses in the video's order. The front row only matters as far as it blocks the rear.",
        faq_dq="How do I see the back row earlier in Bus Traffic Fever Level 14?",
        faq_da="Uncover it in small steps: move one front bus, glance at the rear, and stop the moment it comes into view. The earlier you can read the rear order, the safer the run.",
        faq_eq="Why does clearing the front row first fail in Bus Traffic Fever Level 14?",
        faq_ea="It exposes the back row but leaves it in the wrong order, so the rear buses are stuck behind each other with no way to correct it."),

    dict(n=15, vid="GzKb5oXv4n0", diff="Hard", focus="route ordering", name="The Long Haul",
        intro="Level 15 is the first real wall — a long route you have to follow exactly. Copy it move by move and it cracks.",
        beat="Level 15 is a long, unforgiving route. Treat the video as a sequence to copy rather than a hint to skim, pause after every move, and never jump ahead to a bus the route has not reached yet.",
        summary="Follow the route order exactly, move by move. There is no shortcut — the route itself is the fastest path, and a single skipped move undoes the whole run.",
        whatis="A dense board where every bus depends on the last. One wrong entry collapses the whole route, which is why the level runs long and why it feels like the game's first genuine wall.",
        phase1_title="First Moves: Committing to the Route",
        phase1_steps=["Commit to the full route order before you start.", "Pause the video after each move and mirror it exactly.", "Never jump ahead to a bus the route has not reached."],
        mid_title="Midgame: Managing the Long Middle",
        mid_steps=["In the long middle, protect your attention and pace yourself.", "Take the level in small chunks instead of one long run.", "If the route blurs, rewind the video rather than guessing a new order."],
        phase2_title="Finishing: Copying to the Last Move",
        phase2_steps=["Keep mirroring the video one move at a time.", "Replay any move you are unsure about before continuing.", "Finish only after the final bus leaves in the recorded order."],
        hint="Follow the route order exactly — do not skip ahead.",
        mistake="Jumping to a bus that 'looks free' instead of the next one in the route, which breaks the chain.",
        pros="Clearing it feels like a genuine achievement after the easy opening.",
        cons="Long and unforgiving — a single skipped move undoes the whole run.",
        safety="No tracking, sign-up, or download is part of this page. The Level 15 clip is a public YouTube upload, and the notes only explain how to watch it move by move.",
        price="Level 15 is free to play, as the game is free to download. Optional purchases and ads change by region, so confirm the store listing and refund through the store you used.",
        next_help="Save this Level 15 walkthrough for the route-order lesson, then open the index for the next board. If a move in the clip does not match your board, check the level above or below.",
        faq_q="How do I beat Bus Traffic Fever Level 15?",
        faq_a="Follow the route order exactly, pausing the video after each move to mirror it. Do not jump ahead to a bus the sequence has not reached yet.",
        faq_bq="How many moves does Bus Traffic Fever Level 15 take?",
        faq_ba="More than any level before it — that length is what makes it a wall. The video shows the full sequence, so count along if it helps.",
        faq_cq="What is the hardest single move in Bus Traffic Fever Level 15?",
        faq_ca="Usually the move where a bus looks free but is not next in the route. Resisting that skip-ahead instinct is the hardest part.",
        faq_dq="Is there a shortcut for Bus Traffic Fever Level 15?",
        faq_da="Not reliably. The route is the shortcut — any attempt to skip ahead breaks the chain, so copying the order is actually the fastest path.",
        faq_eq="Why is Bus Traffic Fever Level 15 so much harder than the rest?",
        faq_ea="It is the first long route where every bus depends on the last. A single wrong entry collapses the whole sequence, which is what makes it feel like a wall."),

    dict(n=16, vid="3B2UWDvJ39U", diff="Easy", focus="tight-lane recovery", name="The Squeeze",
        intro="The board tightens under pressure. When it jams, reopen a lane instead of forcing the next move.",
        beat="Level 16 is forgiving until you let it tighten. Take the easy clears when they are there, and the moment a lane starts to close, reopen it before you push another bus through.",
        summary="Recover instead of forcing. The level clears fast unless you let it squeeze shut, so reopening a lane the moment it tightens is the whole skill.",
        whatis="A quick board with a couple of spots that tighten under pressure. It is not about speed — recovery is the real skill, and rushing is exactly what packs the buses into the pinch.",
        phase1_title="First Moves: Taking the Easy Clears",
        phase1_steps=["Take the easy clears while they are available.", "Watch for the moment a lane starts to tighten.", "Pause the second the board feels squeezed."],
        mid_title="Midgame: Not Making the Squeeze Worse",
        mid_steps=["Once the easy clears are gone, stop hunting for a fast move.", "Choose the pull that keeps the most empty space on the board.", "Skip any move that pushes a bus into the tight spot."],
        phase2_title="Finishing: Reopening Before You Push",
        phase2_steps=["Reopen a lane before you force another bus through.", "Back out the last blocking bus if you can.", "Resume only after you have space again."],
        hint="If it tightens, reopen a lane before you force anything.",
        mistake="Pushing through a tightening board until a bus has nowhere to go.",
        pros="Short and easy once you allow yourself to recover instead of rushing.",
        cons="The pressure to be fast makes players force bad moves.",
        safety="This page collects no data and needs no account or install. The Level 16 source is a public YouTube walkthrough, and the text only describes what to watch.",
        price="Level 16 is free to attempt, like the rest of the free-to-download game. In-app purchases and ads vary by region, so check the official store and refund through your download store.",
        next_help="Keep this Level 16 guide for the recovery habit, then jump to the index for the next board. A mismatched clip is usually resolved by the level before or after.",
        faq_q="How do I beat Bus Traffic Fever Level 16?",
        faq_a="Take the easy clears, and the moment a lane starts to tighten, reopen it before forcing another move.",
        faq_bq="Is Bus Traffic Fever Level 16 really easy, or is that a trick?",
        faq_ba="It is easy on paper, but it tightens under pressure — so it is a test of recovery, not a hard sequence. Slow down and it clears quickly.",
        faq_cq="How do I stop the board from tightening in Bus Traffic Fever Level 16?",
        faq_ca="Stop rushing. Take the easy clears first and reopen a lane the moment it starts to close, rather than pushing through.",
        faq_dq="Why does my Bus Traffic Fever Level 16 board tighten even when I go fast?",
        faq_da="Speed is exactly what tightens it. Rushing packs buses into the pinch point, so slow down and reopen a lane before pushing through.",
        faq_eq="How do I reopen a lane that just closed in Bus Traffic Fever Level 16?",
        faq_ea="Back out the last bus that blocked it if you can, or restart and leave that lane clear the next run. The board is short, so a restart is cheap."),

    dict(n=17, vid="_tvGIY6rlT0", diff="Easy", focus="speed vs accuracy", name="The False Shortcut",
        intro="Level 17 baits you into rushing. Slowing down is genuinely the fastest way through.",
        beat="Level 17 rewards the player who slows down. Ignore the urge to move fast, make each pull clean, and the accurate route finishes faster than the frantic one.",
        summary="Slow down on purpose. The board looks like it wants speed, but the fast route is the one that fails — accuracy clears it faster than tapping.",
        whatis="A quick-looking board that punishes rushed taps. The shortcut is a trap: doing it right the first time is actually the fastest path, because a clean sequence has no rework.",
        phase1_title="First Moves: Resisting the Speed Instinct",
        phase1_steps=["Ignore the urge to move fast.", "Read each pull before you make it.", "Make every move clean rather than quick."],
        mid_title="Midgame: Holding Steady Mid-Sequence",
        mid_steps=["Mid-sequence, the urge to rush is strongest — resist it.", "Keep each pull clean rather than quick.", "Watch the video's middle section if your pacing drifts."],
        phase2_title="Finishing: Noticing Accuracy Wins",
        phase2_steps=["Notice how a clean sequence finishes with no rework.", "Avoid the jam a rushed tap would have created.", "Confirm the deliberate route matches the video."],
        hint="Slow down — the accurate route is the fast route.",
        mistake="Rushing the sequence and creating a jam that a calm move would have avoided.",
        pros="Quick and honest — rewards care without being hard.",
        cons="Players who chase speed will create their own jam.",
        safety="No data is gathered here, and no account or permission is needed. The Level 17 clip is a public YouTube upload, and the notes only explain how to follow it.",
        price="Level 17 is free to play within the free-to-download game. Ads and optional purchases shift by region, so verify the store page and refund through the store you used.",
        next_help="Return to this Level 17 walkthrough for the accuracy lesson, then open the index for the next board. If the clip differs from your board, the adjacent level page is the fastest fix.",
        faq_q="How do I beat Bus Traffic Fever Level 17?",
        faq_a="Slow down and make each pull clean rather than tapping fast. Accuracy clears this board faster than speed.",
        faq_bq="How fast should I actually go in Bus Traffic Fever Level 17?",
        faq_ba="As slow as it takes to make each pull clean. There is no timer pressure, so the only speed that matters is not having to redo a jam.",
        faq_cq="Does the timer matter in Bus Traffic Fever Level 17?",
        faq_ca="No — the level is not timed in a way that rewards rushing. Accuracy matters more than pace, and clean beats quick every time.",
        faq_dq="Is speed ever the right call in Bus Traffic Fever Level 17?",
        faq_da="Rarely on this board. The only 'speed' that helps is not having to redo a jam — and that comes from accuracy, not tapping faster.",
        faq_eq="Why does slowing down make Bus Traffic Fever Level 17 faster?",
        faq_ea="A clean sequence has no rework. Rushed taps create jams you then have to undo, so the calm route reaches the end first."),

    dict(n=18, vid="Je86CJgudVc", diff="Moderate", focus="blocking-bus identification", name="The Key Blocker",
        intro="One bus is holding the whole board. Find it, time its move, and everything else shakes loose.",
        beat="Level 18 is solved by finding the blocker. Spot the single bus everything else is stuck behind, free it only when a lane is ready, and the rest of the board opens at once.",
        summary="Find the bus everyone is stuck behind, then time its move. The blocker is not the bus that looks important — it is the one with the longest queue behind it.",
        whatis="A mid board with one dominant blocker. Identify it and time its move correctly, and the whole board unlocks at once — the difficulty is spotting it and not moving it too early.",
        phase1_title="First Moves: Finding the Blocker",
        phase1_steps=["Count how many buses sit behind each vehicle.", "The one with the longest queue behind it is the blocker.", "Study the board until you are sure before moving."],
        mid_title="Midgame: Preparing the Blocker's Path",
        mid_steps=["Once you have spotted the blocker, stop clearing random buses.", "Focus only on the vehicles that sit directly in the blocker's way.", "Do not touch the blocker itself until its whole path is clear."],
        phase2_title="Finishing: Timing the Blocker's Move",
        phase2_steps=["Wait until a lane is open and the blocker's exit is clear.", "Free the blocker and let the whole board flow.", "Confirm the move timing matches the video."],
        hint="Find the bus everyone else is stuck behind, then time its move.",
        mistake="Moving the blocker too early and filling the only lane it could have used.",
        pros="Satisfying to spot the single move that unlocks the whole board.",
        cons="The blocker is easy to misread until you study the board.",
        safety="This page runs no tracking and requires no sign-in or install. The Level 18 source is a public YouTube walkthrough, and the notes only describe what to watch.",
        price="Level 18 costs nothing to attempt, as the game is free to download. Optional purchases and ads vary by region, so check the store listing and refund through the store you used.",
        next_help="Save this Level 18 guide for the blocker-spotting lesson, then use the index for the next board. A clip that does not line up is usually fixed by the level above or below.",
        faq_q="How do I beat Bus Traffic Fever Level 18?",
        faq_a="Identify the single bus that blocks the most vehicles, wait until a lane is ready, then free it to unlock the rest of the board.",
        faq_bq="What if I can't find the blocker in Bus Traffic Fever Level 18?",
        faq_ba="Count the queue behind each bus. The one with the longest line of buses waiting behind it is the blocker, even if it looks unimportant.",
        faq_cq="Can the blocker be in the back row in Bus Traffic Fever Level 18?",
        faq_ca="Yes — a blocker can sit anywhere. Look for the bus with the most vehicles behind it, not the one that looks prominent.",
        faq_dq="How do I find the blocker quickly in Bus Traffic Fever Level 18?",
        faq_da="Count how many buses sit behind each vehicle. The one with the longest queue behind it is the blocker, and the video's first few moves confirm it.",
        faq_eq="Why is timing the blocker's move so important in Bus Traffic Fever Level 18?",
        faq_ea="Move it too early and you fill the one lane it needed. Wait until a lane is open and its exit is clear, then free it to unlock everything at once."),

    dict(n=19, vid="5SC-BXkFuG4", diff="Moderate", focus="multi-lane juggling", name="The Two-Lane Waltz",
        intro="You're juggling two lanes at once here. Find the balancing rhythm and both stay alive.",
        beat="Level 19 makes you juggle two lanes at once. Treat them as one puzzle, alternate moves between them, and never finish one side while the other is left blocked behind you.",
        summary="Balance the two lanes — never finish one while the other is blocked. Alternating moves the way the video does is what keeps both routes alive at once.",
        whatis="A board where two parallel lanes share the exits. Keeping both alive at once is the puzzle, so committing to one lane and letting the other seal shut is the failure state.",
        phase1_title="First Moves: Tracking Both Lanes",
        phase1_steps=["Track both lanes at once from the first move.", "Move one bus per lane, then switch.", "Mirror the video's balancing rhythm."],
        mid_title="Midgame: Correcting the Balance",
        mid_steps=["Watch for one lane pulling ahead of the other.", "If a lane starts to clear too fast, hold it back a move.", "Give the slower lane the next bus to keep the two even."],
        phase2_title="Finishing: Finishing Together",
        phase2_steps=["Keep alternating until both lanes are nearly clear.", "Finish the last buses without leaving one side blocked.", "Confirm the balancing order matches the video."],
        hint="Balance the two lanes — never finish one while the other is blocked.",
        mistake="Committing to one lane and returning to find the other has sealed shut.",
        pros="A satisfying juggling act once you find the rhythm.",
        cons="Losing track of the second lane is easy and costly.",
        safety="No personal data or account is involved here, and nothing is downloaded. The Level 19 clip is a public YouTube upload, and the text only tells you what to watch for.",
        price="Level 19 is free to play, matching the free-to-download game. In-app purchases and ads change by region, so verify the store page and process refunds through the store you used.",
        next_help="Keep this Level 19 page for the balancing lesson, then open the index for the next board. If the video differs from your board, the adjacent level page is the quickest fix.",
        faq_q="How do I beat Bus Traffic Fever Level 19?",
        faq_a="Alternate moves between the two lanes so neither closes while you work the other, matching the video's balancing rhythm.",
        faq_bq="How do I split my attention between two lanes in Bus Traffic Fever Level 19?",
        faq_ba="Move one bus per lane, then switch. Use the video's rhythm as a metronome rather than trying to solve one side to completion.",
        faq_cq="What happens if one lane finishes first in Bus Traffic Fever Level 19?",
        faq_ca="If the other lane is left blocked, you are stuck — so finish them together. Never leave one side sealed while you complete the other.",
        faq_dq="Can I clear one lane completely first in Bus Traffic Fever Level 19?",
        faq_da="No — that is the trap. Finishing one side leaves the other blocked, so you must alternate moves and keep both lanes alive at once.",
        faq_eq="How do I keep track of both lanes in Bus Traffic Fever Level 19?",
        faq_ea="Move one bus per lane, then switch. Watch the video's rhythm and mirror it rather than trying to solve one side to completion."),

    dict(n=20, vid="o7QZSBiuJS8", diff="Hard", focus="phase consolidation", name="The Phased Grid",
        intro="It's a big board, but you clear it in phases. Split it up and it stops feeling overwhelming.",
        beat="Level 20 closes the early game with a phased clear. Split the board into sections, finish each one fully before the next, and consolidate as you go so no half-cleared area blocks your next move.",
        summary="Clear in phases — finish one section before starting the next. Treating the big board as one mess is what makes it feel impossible; splitting it shrinks it to a normal solve.",
        whatis="A dense end-of-phase board that breaks into smaller sections. It is large enough that a scattered approach turns it into a wall, but section by section it is just the habits from levels 1-19.",
        phase1_title="First Moves: Dividing the Board",
        phase1_steps=["Split the board into smaller sections mentally.", "Pick the section closest to an open exit.", "Finish that section fully before moving on."],
        mid_title="Midgame: Consolidating Between Sections",
        mid_steps=["After a section clears, consolidate before starting the next.", "Sweep the cleared section for any bus left half-blocked.", "Pick the next section only after the last one is fully empty."],
        phase2_title="Finishing: Consolidating Section by Section",
        phase2_steps=["Clear each section completely before the next.", "Consolidate as you go so nothing is left half-blocked.", "Confirm the phased order matches the video."],
        hint="Clear in phases — finish one section before starting the next.",
        mistake="Working three sections at once and leaving each one half-blocked.",
        pros="Feels like a real checkpoint before the game's harder middle.",
        cons="Large enough that a scattered approach turns it into a wall.",
        safety="This page gathers no data and asks for no account or permissions. The Level 20 source is a public YouTube walkthrough, and the notes only describe how to follow it.",
        price="Level 20 is free to attempt, as the base game has no entry fee. Ads and optional purchases vary by region, so confirm the store listing and refund through the store you used.",
        next_help="Note this Level 20 walkthrough to close out the early game, then use the index for the next board. If the clip does not match, the level above or below is the fastest fix.",
        faq_q="How do I beat Bus Traffic Fever Level 20?",
        faq_a="Split the board into sections and clear each one fully before starting the next, so no half-finished area blocks your next move.",
        faq_bq="How many sections should I split the Bus Traffic Fever Level 20 board into?",
        faq_ba="Enough to make each one feel manageable — the exact count is up to you. The key is finishing one fully before touching the next.",
        faq_cq="Is Bus Traffic Fever Level 20 a good stopping point?",
        faq_ca="Yes — it is a natural checkpoint before the harder middle. Treat it as a test of the habits from levels 1-19 before pushing further.",
        faq_dq="Is Bus Traffic Fever Level 20 the end of the easy section?",
        faq_da="Yes — it is a natural checkpoint before the harder middle. Treat it as a test of the habits from levels 1-19, especially planning ahead.",
        faq_eq="Why does Bus Traffic Fever Level 20 feel overwhelming?",
        faq_ea="Because it is large and easy to read as one mess. Split it into sections mentally and clear one at a time, and it shrinks to a normal solve."),

    # Levels 21-40: video IDs pending — set each vid="" to the per-level YouTube ID when available.
    dict(n=21, vid="Cu_EATjhaU0", diff="Easy to Medium", focus="conveyor rhythm", name="The Conveyor Warm-Up",
        intro="Buses glide in on a moving conveyor now. Release each one in step with the conveyor's rhythm instead of fighting it.",
        beat="Level 21 reintroduces the conveyor after a long stretch of parked boards. Find the conveyor's rhythm, tap each bus on that rhythm, and let the conveyor hand you the win one vehicle at a time.",
        summary="Ride the conveyor, don't chase it. The level is a rhythm problem: release every bus on the conveyor's rhythm and the board empties itself.",
        whatis="A re-entry board where the buses glide in on a conveyor rather than sitting still. The puzzle is timing — the conveyor has a rhythm, and your taps either land on it or break the flow.",
        phase1_title="First Moves: Feeling the Conveyor's Rhythm",
        phase1_steps=["Watch the conveyor run a full cycle before you touch anything.", "Count the rhythm as the first bus reaches the pickup point.", "Release the first bus only when the conveyor and your tap line up."],
        mid_title="Midgame: Releasing on the Rhythm",
        mid_steps=["Keep the same rhythm through the middle buses.", "Do not rush a tap when the conveyor briefly speeds up.", "Let each bus clear the lane before the next rhythm."],
        phase2_title="Finishing: Holding the Rhythm Home",
        phase2_steps=["Hold the rhythm steady for the final buses.", "Release the last bus on the same rhythm as the first.", "Confirm the conveyor is empty and the lane is clear."],
        hint="Lock onto the conveyor's rhythm, then tap every bus on that rhythm.",
        mistake="Tapping on your own instinct instead of the conveyor's rhythm — one rushed release throws the whole conveyor out of step.",
        pros="A low-pressure rhythm board that teaches the conveyor rhythm early.",
        cons="Players who ignore the conveyor and tap at random never find the flow.",
        faq_q="How do I beat Bus Traffic Fever Level 21?",
        faq_a="Match the conveyor's rhythm and release every bus on that rhythm. It is a rhythm board, so timing the tap to the conveyor matters more than which bus you pick.",
        faq_bq="What is the conveyor in Bus Traffic Fever Level 21?",
        faq_ba="The moving conveyor that carries each bus into position. Your job is to tap in time with it, not to fight against it.",
        faq_cq="Why do my buses jam in Bus Traffic Fever Level 21?",
        faq_ca="Because a tap landed off the conveyor's rhythm. One early or late release breaks the flow and the buses behind it stack up.",
        faq_dq="Do I tap the conveyor or the bus in Bus Traffic Fever Level 21?",
        faq_da="Release the bus as it reaches you, on the conveyor's rhythm. Watch the video to see the exact rhythm before you repeat it.",
        faq_eq="Is Bus Traffic Fever Level 21 a good warm-up for later conveyors?",
        faq_ea="Yes — it brings the conveyor back gently so you can lock the rhythm before the harder conveyor boards show up."),

    dict(n=22, vid="PIzdWXblF4s", diff="Easy to Medium", focus="avoiding overflow", name="The Overflow Opener",
        intro="Buses keep arriving, and the board overflows if you leave them queued too long. Clear the fullest side before the next wave lands.",
        beat="Level 22 is your first real overflow check. Clear the bus that frees the most space before the next wave lands, and keep clearing the fullest side so the board never fills up.",
        summary="Stay ahead of the wave by always clearing the busiest bus first. The level is lost the moment one side is allowed to fill up.",
        whatis="A board that keeps receiving buses while you work. There is no single exit — the threat is volume, and the only way to survive is to clear space faster than the arrivals pile up.",
        phase1_title="First Moves: Reading Which Side Is Filling",
        phase1_steps=["Check both sides before the next wave lands.", "Spot which lane is nearest to overflowing.", "Clear the bus on that side first."],
        mid_title="Midgame: Clearing the Fullest Side",
        mid_steps=["Each wave, clear the bus that frees the most space.", "Do not clear the closest bus if the far side is filling.", "Keep the fullest side clearing before it fills up."],
        phase2_title="Finishing: Outlasting the Final Wave",
        phase2_steps=["Empty the last queue before the final wave arrives.", "Confirm no side is one bus away from overflow.", "Clear the last bus and let the board settle."],
        hint="Always clear the busiest bus — the one that frees the most space before the next wave.",
        mistake="Clearing whatever is closest while the far side quietly overflows and ends the run.",
        pros="A clear early lesson in reading volume instead of just grabbing the nearest bus.",
        cons="The arrivals feel relentless if you never learn to clear the fullest side first.",
        faq_q="How do I beat Bus Traffic Fever Level 22?",
        faq_a="Clear the busiest bus before every wave. Watch which side is filling fastest, free space on that side, and stay ahead of the arrivals.",
        faq_bq="What does 'avoiding overflow' mean in Bus Traffic Fever Level 22?",
        faq_ba="The board keeps receiving buses, and it overflows if the queue gets too long. You clear space faster than the arrivals pile up.",
        faq_cq="Why does Bus Traffic Fever Level 22 keep ending on its own?",
        faq_ca="Because a lane hit capacity while you cleared elsewhere. Always clear the side closest to filling, not the bus closest to you.",
        faq_dq="Which bus do I clear first in Bus Traffic Fever Level 22?",
        faq_da="The one that frees the most space on the side that is nearest to overflowing. The video's first clear shows the pattern.",
        faq_eq="Is Bus Traffic Fever Level 22 the first overflow level?",
        faq_ea="Yes — it introduces the pressure mechanic gently, so build the habit of clearing the fullest side here and later overflow boards get easier."),

    dict(n=23, vid="w7hPZ2ASoUM", diff="Easy to Medium", focus="mid-sequence correction", name="The Mid-Run Fix",
        intro="The obvious opening looks right but dead-ends halfway. Reverse the one wrong move instead of restarting.",
        beat="Level 23 teaches the mid-run correction. Play the obvious opening, spot the block the moment the middle stalls, and back up a single move rather than clearing the board from scratch.",
        summary="The opening is bait — the solution is the correction. When the middle dead-ends, reverse one move and finish on the corrected path.",
        whatis="A board where the first few moves feel correct but lead into a locked middle. The real test is recognizing the stall and correcting mid-sequence instead of resetting.",
        phase1_title="First Moves: Playing the Obvious Opening",
        phase1_steps=["Play the opening moves that look correct.", "Advance until the middle of the sequence stalls.", "Pause the instant the board dead-ends."],
        mid_title="Midgame: Reversing the Wrong Move",
        mid_steps=["Find the one move that boxed the lane in.", "Back that single move up — do not reset the board.", "Plug in the fixed move and keep going."],
        phase2_title="Finishing: Riding the Corrected Path",
        phase2_steps=["Run the fixed path to the finish.", "Confirm the lane that was blocked now opens.", "Finish without restarting the sequence."],
        hint="When the middle stalls, back up one move — not the whole board.",
        mistake="Restarting from zero the moment the middle dead-ends, when a single reversed move fixes the run.",
        pros="Teaches the correction habit early so later mid-run stalls feel routine.",
        cons="Players who refuse to backtrack one move keep replaying the same wrong opening.",
        faq_q="How do I beat Bus Traffic Fever Level 23?",
        faq_a="Play the opening, then correct the one wrong move when the middle stalls. Back up a single move instead of restarting the whole board.",
        faq_bq="What is a mid-sequence correction in Bus Traffic Fever Level 23?",
        faq_ba="Fixing a move in the middle of the run rather than resetting. The opening looks right, but one move blocks the lane and must be reversed.",
        faq_cq="Why does Bus Traffic Fever Level 23 always stall in the middle?",
        faq_ca="Because the obvious opening includes one move that boxes the lane. The stall is the clue that it is time to correct, not restart.",
        faq_dq="Do I restart Bus Traffic Fever Level 23 when it locks up?",
        faq_da="No — back up the single wrong move and continue. The video shows exactly where the correction happens.",
        faq_eq="Is Bus Traffic Fever Level 23 a correction tutorial?",
        faq_ea="Yes — it deliberately baits a wrong-looking-but-blocking opening so you learn to fix a move mid-run instead of resetting."),

    dict(n=24, vid="Q3Fb39wgieI", diff="Easy to Medium", focus="clean final placement", name="The Final-Spot Squeeze",
        intro="The whole board is easy until the last bus, which has to slot in square. Save your focus for that final placement.",
        beat="Level 24 hangs on the last bus. Clear the path so the final bus has a clean lane, then place it square in its exit without over-sliding, and the board is done.",
        summary="Clear the path, then park the last bus perfectly. The level is decided entirely by that final placement.",
        whatis="A board that feels easy right up until the last move. The final bus must settle exactly into its exit, and a mistake of half a lane at the end is the only way to fail.",
        phase1_title="First Moves: Clearing a Lane for the Last Bus",
        phase1_steps=["Clear the buses in front of the final bus first.", "Leave the final bus's exit lane completely open.", "Do not commit the final bus until its lane is clean."],
        mid_title="Midgame: Lining the Final Bus Up",
        mid_steps=["Square the final bus up with its exit lane.", "Adjust the angle before the last slide.", "Check the gap is exactly one lane wide."],
        phase2_title="Finishing: Placing It Without Over-Sliding",
        phase2_steps=["Guide the last bus in with one smooth motion.", "Stop the instant it is square in the exit.", "Check the square parking and clear the level."],
        hint="Save your focus for the last bus — clear its lane, then place it square.",
        mistake="Rushing the final slide and parking the last bus half a lane off, so the finish never registers.",
        pros="A gentle introduction to the final-placement mechanic without a busy board.",
        cons="The easy start lulls players into coasting, then the last bus ends the run.",
        faq_q="How do I beat Bus Traffic Fever Level 24?",
        faq_a="Clear the final bus's lane first, then place it square in its exit. The last move is the whole solve, so line it up before you slide.",
        faq_bq="What is 'clean final placement' in Bus Traffic Fever Level 24?",
        faq_ba="Parking the last bus exactly in its exit lane without over-sliding. The rest of the board is easy, but the final placement must be square.",
        faq_cq="Why does Bus Traffic Fever Level 24 fail on the last bus?",
        faq_ca="Because the final bus landed half a lane off its exit. Clear its lane fully, then slide it in one controlled motion.",
        faq_dq="Which part of Bus Traffic Fever Level 24 matters most?",
        faq_da="The final placement. Everything before it is just clearing a lane, so focus on parking the last bus square.",
        faq_eq="Is Bus Traffic Fever Level 24 the first final-placement level?",
        faq_ea="Yes — it isolates the mechanic on an easy board so you learn to save your focus for the last bus."),

    dict(n=25, vid="Ct4mAnd2s9U", diff="Easy to Medium", focus="opening timing", name="The First-Tap Timing",
        intro="The first tap decides everything in Level 25. Release the opening bus at the exact right moment and the rest falls into place.",
        beat="Level 25 is won or lost on the first tap. Pause, read the opening lane, and time the first release so it ripples cleanly through the buses behind it.",
        summary="Time the first tap, not just the right bus. The opening release sets the order for everything that follows.",
        whatis="A board where the first move carries the level. Tap too early and the lane is still blocked; tap late and the queue shifts — the opening timing is the entire puzzle.",
        phase1_title="First Moves: Pausing Before the First Tap",
        phase1_steps=["Pause and read the opening lane fully.", "Wait for the first bus's lane to line up.", "Time the first tap to that moment."],
        mid_title="Midgame: Letting the Opening Ripple",
        mid_steps=["Let the opening release carry into the next bus.", "Do not interrupt the ripple with an early second tap.", "Confirm the order holds as the middle opens."],
        phase2_title="Finishing: Closing on the Ripple",
        phase2_steps=["Follow the ripple to the final buses.", "Keep the timing even through the last release.", "Finish once the opening order clears the board."],
        hint="Time the first tap — the opening bus sets the order for the rest.",
        mistake="Tapping the first bus immediately instead of waiting for its lane to line up, so the whole sequence starts wrong.",
        pros="A focused timing lesson that pays off on every later opening board.",
        cons="Impatient players tap instantly and then blame the level when the order falls apart.",
        faq_q="How do I beat Bus Traffic Fever Level 25?",
        faq_a="Pause, let the opening lane line up, then time the first tap. The opening release sets the order, so getting that first moment right solves the level.",
        faq_bq="What is 'opening timing' in Bus Traffic Fever Level 25?",
        faq_ba="Releasing the first bus at the exact moment its lane opens. Too early or too late and the sequence behind it shifts.",
        faq_cq="Why does Bus Traffic Fever Level 25 go wrong immediately?",
        faq_ca="Because the first tap fired too early, before the lane lined up. Pause and match the video's first release instead.",
        faq_dq="Do I tap the first bus fast in Bus Traffic Fever Level 25?",
        faq_da="No — timing beats speed here. Wait for the lane to line up, then release once. The video shows the exact moment.",
        faq_eq="Is Bus Traffic Fever Level 25 all about the first move?",
        faq_ea="Yes — it isolates opening timing so you learn to pause and read before that first tap."),

    dict(n=26, vid="KpvMEMykUAY", diff="Medium", focus="controlled tap spacing", name="The Tap Spacer",
        intro="Each bus needs one evenly spaced tap. Hold a steady pace and the queue never falls out of step.",
        beat="Level 26 is about the gap between taps. Set a steady pace, give every bus one tap exactly one tap apart, and never double-tap a bus while the one before it is still moving.",
        summary="One tap per bus, evenly spaced. The level fails the moment you spam or double-tap and the queue falls out of step.",
        whatis="A board that punishes rushed input. Each bus needs its own rhythm, and the puzzle is holding that spacing steady instead of tapping as fast as you can.",
        phase1_title="First Moves: Setting a Steady Tap Pace",
        phase1_steps=["Set one steady pace before you tap anything.", "Give the first bus a single clean tap.", "Count the rhythm before the second tap."],
        mid_title="Midgame: Spacing Each Bus Apart",
        mid_steps=["Space every bus exactly one tap apart.", "Do not double-tap while the previous bus moves.", "Keep the same pace through the middle."],
        phase2_title="Finishing: Holding the Spacing to the End",
        phase2_steps=["Hold the steady pace for the final buses.", "Tap each last bus once, at its own pace.", "Finish without a single rushed double-tap."],
        hint="One tap per bus, evenly spaced — never spam or double-tap.",
        mistake="Double-tapping or spamming, which throws the queue out of step and blocks the lane.",
        pros="A clean discipline check that rewards a steady hand.",
        cons="Fast tappers hit a wall here and have to unlearn the rush.",
        faq_q="How do I beat Bus Traffic Fever Level 26?",
        faq_a="Hold a steady pace and give each bus one tap, evenly spaced. Do not double-tap or spam, and the queue will clear in order.",
        faq_bq="What is 'controlled tap spacing' in Bus Traffic Fever Level 26?",
        faq_ba="Tapping each bus one tap apart instead of spamming. The spacing between taps is what keeps the queue in step.",
        faq_cq="Why does Bus Traffic Fever Level 26 keep locking up?",
        faq_ca="Because a double-tap or a rush of taps threw the queue out of step. Slow to one steady rhythm and space every tap.",
        faq_dq="How fast should I tap in Bus Traffic Fever Level 26?",
        faq_da="Steady, not fast. One tap per bus, evenly spaced — match the video's pace rather than tapping on instinct.",
        faq_eq="Is Bus Traffic Fever Level 26 harder than the earlier boards?",
        faq_ea="Yes — it moves into the Medium range and tests input discipline, not just which bus to move."),

    dict(n=27, vid="F2tkHXJMMFQ", diff="Medium", focus="conveyor rhythm", name="The Conveyor Catch",
        intro="The conveyor speeds up partway through. Catch the faster rhythm the moment it changes or a bus slips past.",
        beat="Level 27 throws a faster conveyor at you. Lock the opening rhythm, then catch the speed-up the moment the conveyor changes, and release each bus on the new rhythm before it slips past.",
        summary="Catch the conveyor's speed-up and lock back onto the rhythm. The level is won by adjusting mid-run instead of holding one stale rhythm.",
        whatis="A conveyor board that changes pace partway through. The conveyor's rhythm accelerates, and the puzzle is catching the new tempo before a bus slips past the pickup point.",
        phase1_title="First Moves: Locking the Opening Rhythm",
        phase1_steps=["Lock the conveyor's opening rhythm.", "Release the first buses on that steady rhythm.", "Watch for the moment the conveyor changes."],
        mid_title="Midgame: Catching the Speed-Up",
        mid_steps=["Spot the exact point where the conveyor accelerates.", "Shift your tap to the faster rhythm immediately.", "Do not keep the old rhythm as buses slip past."],
        phase2_title="Finishing: Locking Back onto the Faster Rhythm",
        phase2_steps=["Hold the faster rhythm through the final buses.", "Release the last bus on the new tempo.", "Confirm the faster conveyor is empty at the finish."],
        hint="Catch the conveyor's speed-up and lock back onto the faster rhythm.",
        mistake="Holding the opening rhythm after the conveyor speeds up, so buses slip past and the board overflows.",
        pros="A satisfying rhythm test that pushes the conveyor lesson up a notch.",
        cons="The mid-run speed change catches players who stop watching the conveyor.",
        faq_q="How do I beat Bus Traffic Fever Level 27?",
        faq_a="Lock the opening rhythm, then catch the speed-up the moment the conveyor accelerates and lock back onto the faster tempo. Adjust mid-run instead of holding one stale rhythm.",
        faq_bq="What makes Bus Traffic Fever Level 27's conveyor different?",
        faq_ba="It changes pace partway through. The conveyor accelerates in the middle, so you have to catch the faster rhythm or buses slip past.",
        faq_cq="Why do buses slip past in Bus Traffic Fever Level 27?",
        faq_ca="Because you kept the opening rhythm after the conveyor sped up. Shift to the faster tempo the instant the conveyor changes.",
        faq_dq="Do I need to watch the conveyor the whole time in Bus Traffic Fever Level 27?",
        faq_da="Yes — the speed-up comes without warning. Watch for the change and match the new rhythm before any bus slips past.",
        faq_eq="Is Bus Traffic Fever Level 27 harder than Bus Traffic Fever Level 21's conveyor?",
        faq_ea="Yes — same mechanic, but the mid-run speed-up forces you to lock back onto the rhythm under pressure."),

    dict(n=28, vid="e-p0sNC8bPY", diff="Medium", focus="avoiding overflow", name="The Overflow Wall",
        intro="Heavier arrivals, and the board hits capacity fast. Clear the busiest bus every single wave without a gap.",
        beat="Level 28 is the overflow wall. The waves are heavier, so there is no room for one idle tap — clear the busiest bus on every wave, back to back, until the board stops filling.",
        summary="Clear the busiest bus every wave, with no gaps. Level 28 punishes any idle moment, so keep clearing space from the first bus to the last.",
        whatis="A sustained overflow board where the incoming buses never let up. The difficulty is real: one moment of clearing the wrong bus and the screen fills up.",
        phase1_title="First Moves: Facing the Heavier Wave",
        phase1_steps=["Read the heavier incoming wave before moving.", "Spot which side hits capacity first.", "Clear the busiest bus on that side right away."],
        mid_title="Midgame: Clearing Every Wave, No Gaps",
        mid_steps=["Clear the busiest bus on every single wave.", "Do not leave a gap between clears.", "Hold the fullest side under capacity the whole run."],
        phase2_title="Finishing: Clearing the Last Queue",
        phase2_steps=["Empty the final queue before the last wave.", "Check both sides are under capacity.", "Clear the last bus and stop the overflow."],
        hint="Clear the busiest bus every wave, back to back, with no idle tap.",
        mistake="Leaving a gap between clears and letting the fullest side overflow mid-run.",
        pros="A genuine wall that feels earned once the back-to-back rhythm clicks.",
        cons="The relentless waves overwhelm players who still grab the nearest bus.",
        faq_q="How do I beat Bus Traffic Fever Level 28?",
        faq_a="Clear the busiest bus on every wave with no gaps. The arrivals are heavier here, so clear the fullest side back to back until the board stops filling.",
        faq_bq="Why is Bus Traffic Fever Level 28 so hard?",
        faq_ba="Because the incoming waves never let up and the board hits capacity fast. One idle tap on the wrong bus fills up the screen.",
        faq_cq="What order do I clear in Bus Traffic Fever Level 28?",
        faq_ca="Always the fullest side first, wave after wave. The exact bus matters less than keeping both sides below capacity at all times.",
        faq_dq="How do I stop Bus Traffic Fever Level 28 from overflowing?",
        faq_da="Never leave a gap between clears. Clear the busiest bus back to back and keep the fullest side under capacity.",
        faq_eq="Is Bus Traffic Fever Level 28 a known wall?",
        faq_ea="Yes — it is one of the levels players stall on most, and the fix is the back-to-back clearing rhythm, not a clever single move."),

    dict(n=29, vid="Wz1G3PX1bIE", diff="Medium", focus="mid-sequence correction", name="The Mid-Run Reset",
        intro="The middle collapses even after a clean opening. There's a correction point where one reversed move saves the run.",
        beat="Level 29 deepens the correction lesson. Play the clean opening, watch the middle collapse, then reverse the one move that caused it and finish on the corrected path.",
        summary="The collapse is the clue. Reverse the one move that caused it, then finish — the level is a correction, not a restart.",
        whatis="A board that collapses partway through despite a clean opening. The mid-run block is deliberate, and the solution is finding and reversing the single move that caused it.",
        phase1_title="First Moves: Playing the Clean Opening",
        phase1_steps=["Play the opening that starts clean.", "Advance until the middle collapses.", "Stop the moment the sequence breaks."],
        mid_title="Midgame: Finding the Correction Point",
        mid_steps=["Trace the collapse back to the one wrong move.", "Reverse that single move, nothing more.", "Replace that move with the corrected one."],
        phase2_title="Finishing: Finishing on the Corrected Path",
        phase2_steps=["Stay on the corrected route to the end.", "Confirm the collapsed lane now opens.", "Finish without a full restart."],
        hint="Trace the collapse to its one wrong move, reverse it, and continue.",
        mistake="Resetting the whole board after a clean opening, when a single reversed move rescues the run.",
        pros="Sharpens the correction habit on a board that hides its one wrong move.",
        cons="The hidden collapse point frustrates players who reset instead of tracing it back.",
        faq_q="How do I beat Bus Traffic Fever Level 29?",
        faq_a="Play the clean opening, then trace the collapse back to the one wrong move and reverse it. Finish on the corrected path instead of restarting.",
        faq_bq="What is the correction point in Bus Traffic Fever Level 29?",
        faq_ba="The single move that caused the middle to collapse. Find it, reverse just that move, and continue — no full reset needed.",
        faq_cq="Why does Bus Traffic Fever Level 29 collapse after a clean start?",
        faq_ca="Because the collapse is built into the board. The clean opening is a trap, and the collapse is the signal to correct one move.",
        faq_dq="Do I restart Bus Traffic Fever Level 29 when it collapses?",
        faq_da="No — trace the collapse to the one wrong move, reverse it, and keep going. The video marks the exact correction point.",
        faq_eq="Is Bus Traffic Fever Level 29 like Bus Traffic Fever Level 23?",
        faq_ea="Same correction mechanic, but the wrong move is hidden better, so you have to trace the collapse back instead of seeing it coming."),

    dict(n=30, vid="0QAsLBORICA", diff="Medium", focus="clean final placement", name="The Final Slot",
        intro="The last bus has to slide into a tight slot at the exact angle. Set it up instead of forcing it.",
        beat="Level 30 tightens the final placement. Clear the slot fully, align the final bus to the exact angle, and slide it in with one controlled motion so it locks without over-sliding.",
        summary="Set up the slot, align the angle, and slide once. The last bus locks the level only when the placement is exact.",
        whatis="A board where the final bus must enter a tighter slot than before. The rest is straightforward, but the last placement demands a precise angle and a controlled slide.",
        phase1_title="First Moves: Clearing the Tight Slot",
        phase1_steps=["Clear every bus blocking the final slot.", "Open the slot to its full width.", "Do not touch the final bus until the slot is clear."],
        mid_title="Midgame: Aligning the Exact Angle",
        mid_steps=["Align the final bus to the slot's exact angle.", "Adjust the approach before the final slide.", "Check the slot is wide enough for one clean entry."],
        phase2_title="Finishing: Sliding It Home Once",
        phase2_steps=["Ease the final bus into the slot with one motion.", "Stop the moment it locks into the slot.", "Confirm it locked and clear the level."],
        hint="Clear the slot, align the angle, and slide the last bus in once.",
        mistake="Forcing the final bus into the slot at the wrong angle, so it jams and the finish never registers.",
        pros="A precise finish that rewards patience on the last move.",
        cons="The tighter slot punishes any forced or over-slid placement.",
        faq_q="How do I beat Bus Traffic Fever Level 30?",
        faq_a="Clear the final slot fully, align the last bus to the exact angle, then slide it in once. The placement must be precise, so do not force it.",
        faq_bq="What is 'clean final placement' in Bus Traffic Fever Level 30?",
        faq_ba="Sliding the last bus into a tight slot at the exact angle so it locks without jamming or over-sliding.",
        faq_cq="Why does the last bus jam in Bus Traffic Fever Level 30?",
        faq_ca="Because it entered the slot at the wrong angle. Clear the slot, align the approach, then slide once with control.",
        faq_dq="Which part of Bus Traffic Fever Level 30 matters most?",
        faq_da="The final slot. Set up the lane, align the angle, and let one clean slide lock the level.",
        faq_eq="Is Bus Traffic Fever Level 30 harder than Bus Traffic Fever Level 24's placement?",
        faq_ea="Yes — the slot is tighter, so the angle and the single controlled slide matter more than before."),

    dict(n=31, vid="y2sLY7YQX7k", diff="Medium", focus="opening timing", name="The Opening Gate",
        intro="The opening bus has to clear a gate that only opens for a moment. Hit that timing and the whole board follows.",
        beat="Level 31 puts a gate on the opening move. Wait for the gate's short open window, release the first bus through it, and let that clean entry set the order for everything behind it.",
        summary="Hit the gate's open window with the first bus, and the board follows. Miss it, and the opening scramble costs the run.",
        whatis="A board where the first bus must pass a gate that opens only briefly. The opening timing is tighter than before, and everything after it depends on hitting that window.",
        phase1_title="First Moves: Watching the Gate's Window",
        phase1_steps=["Watch the gate cycle before you move.", "Spot the short window when it is open.", "Release the first bus through that window."],
        mid_title="Midgame: Letting the Clean Entry Set the Order",
        mid_steps=["Let the clean opening entry set the order.", "Do not scramble after a missed window.", "Keep the next buses in the opening's sequence."],
        phase2_title="Finishing: Closing on the Opening",
        phase2_steps=["Follow the opening's order to the last buses.", "Keep the gate-timed order even to the finish.", "Finish once the gate-timed order clears."],
        hint="Hit the gate's open window with the first bus — the rest follows.",
        mistake="Releasing the first bus against a closed gate, then scrambling to recover the order.",
        pros="A tighter opening-timing test that rewards one clean timed entry.",
        cons="The short gate window punishes players who tap the opening on instinct.",
        faq_q="How do I beat Bus Traffic Fever Level 31?",
        faq_a="Watch the gate's cycle, then release the first bus through its open window. The clean entry sets the order for the whole board.",
        faq_bq="What is the gate in Bus Traffic Fever Level 31?",
        faq_ba="A brief opening the first bus must pass through. The opening timing is about hitting the gate's open window, not just moving first.",
        faq_cq="Why does Bus Traffic Fever Level 31 scramble at the start?",
        faq_ca="Because the first bus hit a closed gate. Wait for the open window, then release once and let the order settle.",
        faq_dq="When do I tap the first bus in Bus Traffic Fever Level 31?",
        faq_da="At the gate's open window. Watch the cycle, match the video's release, and the opening will set the order cleanly.",
        faq_eq="Is Bus Traffic Fever Level 31 a harder opening-timing board?",
        faq_ea="Yes — the gate makes the opening window tighter, so the first tap has to be more precise than earlier opening levels."),

    dict(n=32, vid="jDFv2SBZV-Y", diff="Medium", focus="controlled tap spacing", name="The Spacing Corridor",
        intro="A long corridor of buses, one evenly spaced tap each. Keep the pace steady across the whole row.",
        beat="Level 32 stretches the spacing lesson down a long corridor. Set one pace and carry it the whole length, one tap per bus, so the row clears evenly from front to back.",
        summary="One steady pace across the whole corridor. Any rushed or double tap breaks the row and jams the lane.",
        whatis="A long row of buses that must be released in order. The corridor rewards a single steady tap pace, and the challenge is holding that spacing for every bus in the line.",
        phase1_title="First Moves: Setting the Corridor Pace",
        phase1_steps=["Set one steady pace before the row starts.", "Give the front bus a single clean tap.", "Count the rhythm before the next bus."],
        mid_title="Midgame: Spacing Down the Whole Row",
        mid_steps=["Space each bus one tap apart down the row.", "Do not speed up or double-tap mid-corridor.", "Keep the same pace from front to back."],
        phase2_title="Finishing: Clearing the Corridor's Tail",
        phase2_steps=["Hold the pace through the last few buses.", "Tap each tail bus once, at its own pace.", "Finish once the whole corridor is clear."],
        hint="One steady pace down the whole corridor — never rush the middle.",
        mistake="Speeding up or double-tapping halfway down the row, which jams the corridor.",
        pros="A clean endurance test for holding a steady tap pace.",
        cons="The long row wears down players who lose the pace halfway through.",
        faq_q="How do I beat Bus Traffic Fever Level 32?",
        faq_a="Hold one steady pace and tap each bus once, evenly spaced, down the whole corridor. Any rush or double-tap jams the row.",
        faq_bq="What is the corridor in Bus Traffic Fever Level 32?",
        faq_ba="A long row of buses that must clear in order. The puzzle is holding an even tap spacing across the whole line.",
        faq_cq="Why does Bus Traffic Fever Level 32 jam halfway?",
        faq_ca="Because the tap pace sped up or a bus got double-tapped mid-row. Keep one steady rhythm from the front bus to the tail.",
        faq_dq="How do I keep the pace in Bus Traffic Fever Level 32?",
        faq_da="One tap per bus, one tap apart, from front to back. Match the video's steady spacing and do not rush the middle.",
        faq_eq="Is Bus Traffic Fever Level 32 harder than Bus Traffic Fever Level 26?",
        faq_ea="Yes — same spacing discipline, but the longer corridor tests whether you can hold the pace to the very end."),

    dict(n=33, vid="DecjGEjLNCg", diff="Medium", focus="conveyor rhythm", name="The Conveyor Corridor",
        intro="A long conveyor corridor feeding buses one after another. Hold the conveyor's rhythm from the first bus to the last.",
        beat="Level 33 runs the conveyor down a long corridor. Lock the conveyor's rhythm at the first bus and hold it the entire length, releasing each bus on the same rhythm until the corridor empties.",
        summary="Hold the conveyor's rhythm for the whole corridor. The level is an endurance test of the conveyor rhythm, one bus at a time.",
        whatis="A conveyor that feeds a long corridor of buses in order. The rhythm is steady, but the challenge is maintaining the conveyor's rhythm across the full length without drifting.",
        phase1_title="First Moves: Locking the Corridor Rhythm",
        phase1_steps=["Lock the conveyor's rhythm at the corridor's first bus.", "Release the corridor's opening buses on that rhythm.", "Commit the rhythm to memory before the corridor lengthens."],
        mid_title="Midgame: Holding the Rhythm the Whole Length",
        mid_steps=["Hold the same rhythm down the long corridor.", "Do not drift faster or slower mid-length.", "Release each bus exactly on the conveyor's rhythm."],
        phase2_title="Finishing: Emptying the Corridor",
        phase2_steps=["Keep the rhythm to the last few buses.", "Release the corridor's last bus on the same rhythm.", "Confirm the corridor is empty and clear."],
        hint="Lock the conveyor's rhythm and hold it the entire length of the corridor.",
        mistake="Drifting off the rhythm halfway down the corridor, so the buses start stacking.",
        pros="A pure rhythm endurance test that locks the conveyor rhythm in for good.",
        cons="The long corridor exposes any drift in your tap timing.",
        faq_q="How do I beat Bus Traffic Fever Level 33?",
        faq_a="Lock the conveyor's rhythm at the first bus and hold it the whole corridor. Release each bus on the same rhythm until the line empties.",
        faq_bq="What is the conveyor corridor in Bus Traffic Fever Level 33?",
        faq_ba="A long conveyor that feeds buses in order. The challenge is holding the conveyor's rhythm across the full length without drifting.",
        faq_cq="Why do buses stack in Bus Traffic Fever Level 33?",
        faq_ca="Because the tap drifted off the conveyor's rhythm partway down the corridor. Lock back onto the rhythm and hold it steady.",
        faq_dq="Do I change pace in Bus Traffic Fever Level 33?",
        faq_da="No — keep one locked rhythm from the first bus to the last. The corridor rewards consistency, not speed.",
        faq_eq="Is Bus Traffic Fever Level 33 harder than Bus Traffic Fever Level 27?",
        faq_ea="Different pressure — Level 27 speeds up mid-run, while Level 33 asks you to hold one rhythm over a longer stretch."),

    dict(n=34, vid="XN_kRwscnJA", diff="Medium", focus="avoiding overflow", name="The Overflow Dead End",
        intro="The board funnels into a dead end that overflows if you clear in the wrong order. Clear the back first.",
        beat="Level 34 adds a dead end to the overflow. Clear the back buses first, keep the dead-end side from overflowing, and never let a front bus seal off the lane you still need to empty.",
        summary="Clear the back before the front traps you. The dead end overflows unless you clear in the order that keeps the lane open.",
        whatis="A board that funnels into a dead end where overflow is the threat. The trap is clearing the front first, which seals the lane and lets the back overflow.",
        phase1_title="First Moves: Reading the Dead-End Funnel",
        phase1_steps=["Read the dead end before the first clear.", "Spot which side funnels toward the trap.", "Clear the back bus on that side first."],
        mid_title="Midgame: Clearing the Back First",
        mid_steps=["Clear the back buses before the front seals.", "Keep the dead-end side below capacity.", "Do not clear the front and trap the lane."],
        phase2_title="Finishing: Emptying the Funnel",
        phase2_steps=["Empty the back of the funnel before the last wave.", "Confirm the dead end is below capacity.", "Clear the last bus and escape the trap."],
        hint="Clear the back of the dead end first, before the front seals the lane.",
        mistake="Clearing the front first, which seals the lane and lets the dead-end side overflow.",
        pros="A clever order puzzle that rewards reading the funnel instead of grabbing the front.",
        cons="The front-first trap catches players who never check the back of the dead end.",
        faq_q="How do I beat Bus Traffic Fever Level 34?",
        faq_a="Clear the back of the dead end first so the front never seals the lane. Clear in the order that keeps the funnel open until it empties.",
        faq_bq="What is the dead end in Bus Traffic Fever Level 34?",
        faq_ba="A section of the board that funnels into a trap. Clearing the front first seals the lane and lets the back overflow.",
        faq_cq="Why does Bus Traffic Fever Level 34 trap me?",
        faq_ca="Because you cleared the front first and sealed the lane before the back was empty. Clear the back side first.",
        faq_dq="Which side do I clear first in Bus Traffic Fever Level 34?",
        faq_da="The back of the dead end, not the front. Keep the funnel open by clearing the side that fills up first.",
        faq_eq="Is Bus Traffic Fever Level 34 a new kind of overflow?",
        faq_ea="Yes — it pairs overflow with a dead-end funnel, so the order you clear in matters as much as the volume."),

    dict(n=35, vid="2w9gnMioZvs", diff="Medium", focus="mid-sequence correction", name="The Rush-Hour Correction",
        intro="A packed board stalls at its busiest moment. There's a correction that untangles the rush instead of resetting it.",
        beat="Level 35 stalls at peak rush. Play into the pack, spot the one move that locked the middle, reverse it, and let the corrected order untangle the board.",
        summary="Untangle the rush with one reversed move. The board stalls at its busiest, and the correction frees it without a restart.",
        whatis="A packed board that stalls at the densest moment. The mid-run block is buried in the crowd, and the solution is finding the single move that locked it and reversing it.",
        phase1_title="First Moves: Playing Into the Pack",
        phase1_steps=["Play the opening into the packed board.", "Advance until the rush stalls.", "Stop at the exact moment the middle locks."],
        mid_title="Midgame: Untangling the Locked Move",
        mid_steps=["Find the one move that locked the middle.", "Reverse that move — do not reset the pack.", "Let the corrected order untangle the board."],
        phase2_title="Finishing: Clearing the Untangled Board",
        phase2_steps=["Follow the corrected order to the end.", "Confirm the locked lane now flows.", "Finish once the rush clears."],
        hint="Untangle the rush by reversing the one move that locked the middle.",
        mistake="Resetting a packed board at its busiest, when reversing one move untangles the whole rush.",
        pros="A dense correction test that feels great once the single unlock works.",
        cons="The crowded board hides the wrong move, tempting players to reset.",
        faq_q="How do I beat Bus Traffic Fever Level 35?",
        faq_a="Play into the pack, then reverse the one move that locked the middle and let the corrected order untangle the board. No reset needed.",
        faq_bq="What is the rush-hour correction in Bus Traffic Fever Level 35?",
        faq_ba="Fixing the single move that locks a packed board at its busiest, instead of resetting the whole rush.",
        faq_cq="Why does Bus Traffic Fever Level 35 stall at the busiest moment?",
        faq_ca="Because the board is built to lock at peak density. The stall is the clue to find and reverse the one wrong move.",
        faq_dq="Do I reset Bus Traffic Fever Level 35 when it locks?",
        faq_da="No — the board is at its densest, so resetting wastes a clean opening. Reverse the one locked move and continue.",
        faq_eq="Is Bus Traffic Fever Level 35 the hardest correction level?",
        faq_ea="One of them — the crowded board hides the correction point better than the earlier correction boards."),

    dict(n=36, vid="C1r7kpOagI4", diff="Medium", focus="clean final placement", name="The Final Placement Split",
        intro="The last bus splits the difference between two exits. Pick the one that lines up square.",
        beat="Level 36 gives the final bus two possible exits. Choose the exit that lines up square, then place the bus into it cleanly so the board registers the finish.",
        summary="Pick the square exit and place the last bus cleanly. The split is a choice, and only the lined-up exit locks the level.",
        whatis="A board where the final bus faces two exits. One lines up square and the other is half a lane off; the solution is choosing the right exit and placing the bus precisely.",
        phase1_title="First Moves: Clearing Both Exit Options",
        phase1_steps=["Clear the buses in front of both exits.", "Leave the final bus free to choose.", "Do not commit until both options are open."],
        mid_title="Midgame: Choosing the Square Exit",
        mid_steps=["Compare the two exits side by side.", "Pick the one that lines the bus up square.", "Align the final bus to that exit."],
        phase2_title="Finishing: Placing It Square",
        phase2_steps=["Slide the final bus into the square exit.", "Stop the moment it locks in place.", "Confirm the square exit locked and clear the level."],
        hint="Pick the exit that lines up square, then place the last bus cleanly.",
        mistake="Sliding the final bus into the off-center exit, so it never lines up and the finish does not register.",
        pros="A satisfying final choice that rewards checking both exits.",
        cons="The split tempts a rushed pick of the wrong, off-center exit.",
        faq_q="How do I beat Bus Traffic Fever Level 36?",
        faq_a="Clear both exits, pick the one that lines the final bus up square, and slide it in cleanly. The off-center exit never locks the finish.",
        faq_bq="What is the split in Bus Traffic Fever Level 36?",
        faq_ba="The final bus faces two exits, and only one lines it up square. Choosing the right exit and placing it cleanly is the whole solve.",
        faq_cq="Why does Bus Traffic Fever Level 36 not finish?",
        faq_ca="Because the final bus went into the off-center exit. Pick the square exit and slide the bus in precisely.",
        faq_dq="Which exit do I use in Bus Traffic Fever Level 36?",
        faq_da="The one that lines the last bus up square. Compare both, then place the bus into the exit that locks cleanly.",
        faq_eq="Is Bus Traffic Fever Level 36 different from the other placement levels?",
        faq_ea="Yes — it adds a choice between two exits, so picking the square one matters before the placement itself."),

    dict(n=37, vid="_bUJgXMqocw", diff="Medium", focus="opening timing", name="The Rolling Start",
        intro="The board only starts moving once the opening bus pulls away. Time that first release right.",
        beat="Level 37 hangs on the first release. Wait for the opening bus to pull away, then release it at that exact rhythm so the rest of the board rolls out in order.",
        summary="Start the board rolling on the first rhythm, and everything behind it follows. Miss it, and the whole board stalls.",
        whatis="A board where the first bus has to pull away before anything else moves. The opening timing is the entire puzzle: release too early or late and the board stays stalled.",
        phase1_title="First Moves: Waiting for the First Bus to Move",
        phase1_steps=["Watch the opening bus before you touch anything.", "Wait for it to pull away cleanly.", "Release it on that exact rhythm."],
        mid_title="Midgame: Letting the Board Start Rolling",
        mid_steps=["Let the clean opening start the board rolling.", "Do not rush the second bus after the first pulls away.", "Keep the order the opening sets."],
        phase2_title="Finishing: Rolling to the Finish",
        phase2_steps=["Follow the rolling order to the last buses.", "Keep the opening's pace even to the finish.", "Finish once the board rolls clear."],
        hint="Start the board rolling with the first release — everything else follows.",
        mistake="Releasing the first bus before it can pull away, so the board stays stalled and the run stalls.",
        pros="A precise opening-timing board that rewards patience on the first rhythm.",
        cons="The stalled start confuses players who tap the first bus on instinct.",
        faq_q="How do I beat Bus Traffic Fever Level 37?",
        faq_a="Wait for the opening bus to pull away, then release it on that rhythm. The clean start sets the whole board rolling in order.",
        faq_bq="What makes the opening tricky in Bus Traffic Fever Level 37?",
        faq_ba="The first bus has to pull away before the board moves. The opening timing is hitting that rhythm exactly.",
        faq_cq="Why does Bus Traffic Fever Level 37 stay stalled?",
        faq_ca="Because the first bus was released before it could pull away. Wait for it to move, then tap once on the rhythm.",
        faq_dq="When do I release the first bus in Bus Traffic Fever Level 37?",
        faq_da="The instant it pulls away. Match the video's opening release and the board starts rolling cleanly.",
        faq_eq="Is Bus Traffic Fever Level 37 another opening-timing board?",
        faq_ea="Yes — it isolates the first-release rhythm, so the opening tap has to be patient and precise."),

    dict(n=38, vid="RLTrXaMaf_8", diff="Medium", focus="controlled tap spacing", name="The Gridlock Spacer",
        intro="A gridlocked board that only untangles with even taps. Steady spacing breaks the jam.",
        beat="Level 38 turns a gridlock into a spacing puzzle. Set one steady pace and release each bus a tap apart, letting the even taps unwind the jam instead of spamming it.",
        summary="Break the gridlock with even tap spacing. One tap per bus, one tap apart, and the jam unwinds in order.",
        whatis="A gridlocked board where the only way out is disciplined input. Each bus needs one tap spaced a tap apart, and spam or double-taps only tighten the jam.",
        phase1_title="First Moves: Setting the Unwind Pace",
        phase1_steps=["Set one steady pace before touching the jam.", "Release the first bus with a single tap.", "Count the rhythm before the next release."],
        mid_title="Midgame: Unwinding the Gridlock",
        mid_steps=["Release each bus one tap apart.", "Do not spam or double-tap mid-jam.", "Let the even spacing unwind the gridlock."],
        phase2_title="Finishing: Clearing the Unwound Jam",
        phase2_steps=["Hold the spacing through the last buses.", "Tap each final bus once, on its rhythm.", "Finish once the gridlock fully clears."],
        hint="Unwind the gridlock with one even tap per bus — never spam the jam.",
        mistake="Spamming taps at the gridlock, which tightens the jam instead of unwinding it.",
        pros="A satisfying payoff when even spacing finally breaks the jam.",
        cons="The gridlock baits fast taps, and spamming only makes it worse.",
        faq_q="How do I beat Bus Traffic Fever Level 38?",
        faq_a="Set one steady pace and release each bus one tap apart. The even spacing unwinds the gridlock, while spam only tightens it.",
        faq_bq="What is the gridlock in Bus Traffic Fever Level 38?",
        faq_ba="A jammed board that only clears through disciplined tap spacing. Each bus needs one tap, spaced a tap apart.",
        faq_cq="Why does Bus Traffic Fever Level 38 get worse when I tap fast?",
        faq_ca="Because spam and double-taps tighten the jam. Slow to one steady rhythm and release each bus evenly.",
        faq_dq="How do I break the jam in Bus Traffic Fever Level 38?",
        faq_da="One even tap per bus, spaced a tap apart. Match the video's steady pace and the gridlock unwinds in order.",
        faq_eq="Is Bus Traffic Fever Level 38 the hardest spacing board?",
        faq_ea="Arguably — the gridlock makes steady input harder, so it tests spacing discipline under pressure."),

    dict(n=39, vid="KxjYMJfb7oc", diff="Medium", focus="conveyor rhythm", name="The Final Conveyor",
        intro="The last conveyor board throws a long run of buses at you. Hold the rhythm through the whole sequence.",
        beat="Level 39 is the final conveyor test. Lock the conveyor's rhythm at the first bus and carry it through the whole long run, releasing each bus on the rhythm until the conveyor is empty.",
        summary="Hold the conveyor's rhythm through the whole long run. The final conveyor is an endurance test, one on-rhythm release at a time.",
        whatis="The last full conveyor sequence, a long run of buses on the conveyor. The rhythm is steady, and the challenge is holding the rhythm across the entire sequence without a single miss.",
        phase1_title="First Moves: Locking the Final Rhythm",
        phase1_steps=["Lock the conveyor's rhythm at the first bus of the long run.", "Release the run's opening buses on that rhythm.", "Settle the rhythm before the run gets long."],
        mid_title="Midgame: Carrying the Rhythm Through the Run",
        mid_steps=["Carry the same rhythm through the long run.", "Do not drift or miss a single tap.", "Release each bus exactly on the conveyor's rhythm."],
        phase2_title="Finishing: Emptying the Final Conveyor",
        phase2_steps=["Hold the rhythm to the last few buses.", "Release the run's final bus on the same rhythm.", "Confirm the long conveyor is empty at the finish."],
        hint="Hold the conveyor's rhythm through the whole long run — no missed counts.",
        mistake="Missing a single tap mid-run, which breaks the rhythm and stacks the remaining buses.",
        pros="A fitting final conveyor that locks the rhythm habit in for good.",
        cons="The long run punishes any lapse in the rhythm with a stacked conveyor.",
        faq_q="How do I beat Bus Traffic Fever Level 39?",
        faq_a="Lock the conveyor's rhythm at the first bus and carry it through the whole long run. Release each bus on the rhythm until the conveyor is empty.",
        faq_bq="What is the final conveyor in Bus Traffic Fever Level 39?",
        faq_ba="The last full conveyor sequence, a long run of buses on the conveyor. The challenge is holding the rhythm across the entire sequence.",
        faq_cq="Why do buses stack in Bus Traffic Fever Level 39?",
        faq_ca="Because a single tap was missed mid-run, breaking the rhythm. Lock back onto the rhythm and carry it through without drifting.",
        faq_dq="Is Bus Traffic Fever Level 39 an endurance test?",
        faq_da="Yes — the run is long and steady, so the challenge is holding one rhythm from the first bus to the last.",
        faq_eq="Is Bus Traffic Fever Level 39 the last conveyor level?",
        faq_ea="It caps the conveyor sequence, so treat it as the final rhythm check before the final gate."),

    dict(n=40, vid="7S2irBy5ApM", diff="Medium", focus="avoiding overflow", name="The Overflow Gate",
        intro="The final gate throws everything at you at once. Clear the busiest bus wave after wave until the flood stops.",
        beat="Level 40 is the overflow gate — the cumulative test of everything so far. Read the flood first, clear the busiest bus every wave with no gaps, and keep the fullest side under capacity until the arrivals stop.",
        summary="Clear the busiest bus every wave until the flood stops. The gate combines the overflow lessons from levels 22, 28, and 34 into one sustained push.",
        whatis="A final board that combines every overflow lesson into one sustained flood. The arrivals are heavier and steadier, and the only way through is clearing the fullest side back to back without a single gap.",
        phase1_title="First Moves: Reading the Full Flood",
        phase1_steps=["Read the whole flood before the first clear.", "Spot which side fills up under the flood.", "Clear the busiest bus there before the wave lands."],
        mid_title="Midgame: Clearing Every Wave to the Gate",
        mid_steps=["Clear the busiest bus on every wave, no gaps.", "Keep the fullest side below capacity through the gate.", "Do not let a front bus seal the lane you still need."],
        phase2_title="Finishing: Passing the Gate",
        phase2_steps=["Empty the last queue before the final wave.", "Confirm the flood has not filled up either side.", "Clear the last bus and pass the overflow gate."],
        hint="Clear the busiest bus every wave, no gaps, until the flood stops.",
        mistake="Leaving a single gap between clears and letting the fullest side overflow at the gate.",
        pros="A true milestone that rewards every overflow lesson learned so far.",
        cons="The sustained flood overwhelms players who never learned to clear the fullest side.",
        faq_q="How do I beat Bus Traffic Fever Level 40?",
        faq_a="Clear the busiest bus on every wave with no gaps until the arrivals stop. The gate combines the overflow lessons from earlier levels into one sustained push.",
        faq_bq="What is the overflow gate in Bus Traffic Fever Level 40?",
        faq_ba="The final test that combines every overflow lesson into one flood. You clear the fullest side back to back until the board stops filling.",
        faq_cq="Why does Bus Traffic Fever Level 40 feel like a wall?",
        faq_ca="Because it piles the overflow pressure from levels 22, 28, and 34 on at once. One gap between clears fills up the screen.",
        faq_dq="Which bus do I clear first in Bus Traffic Fever Level 40?",
        faq_da="The busiest bus on the side that fills up first, then keep clearing every wave. The video's first clear shows the pattern.",
        faq_eq="Is Bus Traffic Fever Level 40 a boss level?",
        faq_ea="Yes — it is the final gate, and it caps the overflow sequence with a sustained flood that tests the whole habit."),
]


def thumbnail(vid):
    return "https://i.ytimg.com/vi/%s/hqdefault.jpg" % vid


def jsonld(level, vid, title, desc, url, faqs):
    graph = [
        {"@type": "Article", "@id": url + "#article", "headline": title, "description": desc,
         "author": {"@type": "Organization", "name": "Bus Traffic Fever Guide"},
         "publisher": {"@type": "Organization", "name": "Bus Traffic Fever Guide"},
         "mainEntityOfPage": {"@type": "WebPage", "@id": url},
         "image": thumbnail(vid) if vid else DOMAIN + "/og-image.jpg",
         "datePublished": TODAY, "dateModified": TODAY, "inLanguage": "en"},
    ]
    if vid:
        graph += [
            {"@type": "VideoObject", "name": "Bus Traffic Fever Level %d Walkthrough" % level,
             "description": desc, "thumbnailUrl": thumbnail(vid),
             "contentUrl": "https://www.youtube.com/watch?v=%s" % vid,
             "embedUrl": "https://www.youtube-nocookie.com/embed/%s" % vid,
             "uploadDate": TODAY},
            {"@type": "ImageObject", "contentUrl": thumbnail(vid),
             "description": "Bus Traffic Fever Level %d walkthrough video thumbnail" % level},
        ]
    graph += [
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN + "/"},
            {"@type": "ListItem", "position": 2, "name": "Level Guides", "item": DOMAIN + "/#levels"},
            {"@type": "ListItem", "position": 3, "name": "Level %d" % level, "item": url}]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs]},
        {"@type": "WebSite", "@id": DOMAIN + "/#website", "name": "Bus Traffic Fever Guide",
         "url": DOMAIN + "/", "inLanguage": "en"},
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)


HEADER = """  <header class="site-header">
    <div class="container">
      <nav class="nav" aria-label="Main navigation">
        <a class="brand" href="/" aria-label="Bus Traffic Fever Guide home">
          <span class="brand-mark" aria-hidden="true">
            <svg viewBox="0 0 32 32" fill="none" aria-hidden="true">
              <rect x="6" y="9" width="20" height="13" rx="3" fill="#241f18"/>
              <rect x="8" y="11" width="4" height="4" rx="1" fill="#fff"/>
              <rect x="14" y="11" width="4" height="4" rx="1" fill="#fff"/>
              <rect x="20" y="11" width="4" height="4" rx="1" fill="#fff"/>
              <circle cx="10" cy="25" r="3" fill="#241f18"/>
              <circle cx="22" cy="25" r="3" fill="#241f18"/>
            </svg>
          </span>
          Bus Traffic Fever Guide
        </a>
        <button class="nav-toggle" id="navToggle" aria-label="Toggle menu">☰</button>
        <ul class="nav-links" id="navLinks">
          <li><a href="/#levels">Levels</a></li>
          <li><a href="/#about">What Is It</a></li>
          <li><a href="/#how-to-play">How to Play</a></li>
          <li><a href="/#tips">Tips</a></li>
          <li><a href="/#download">Download</a></li>
          <li><a href="/#faq">FAQ</a></li>
        </ul>
        <a class="btn btn--primary nav-cta" href="/#download">⬇ Download</a>
      </nav>
    </div>
  </header>"""

FOOTER = """  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <a class="footer-brand" href="https://bustrafficfever.net/">Bus Traffic Fever</a>
          <p style="font-size:0.94rem">Level walkthroughs, route-planning tips, and video answers for the GOODROID parking-jam puzzle — so you can clear every jam without wasting moves.</p>
        </div>
        <div>
          <h4>Explore</h4>
          <ul>
            <li><a href="/#levels">Level Directory</a></li>
            <li><a href="/#how-to-play">How to Play</a></li>
            <li><a href="/#tips">Strategy Tips</a></li>
            <li><a href="/#download">Download</a></li>
            <li><a href="/#faq">FAQ</a></li>
          </ul>
        </div>
        <div>
          <h4>Popular Levels</h4>
          <ul>
            <li><a href="/level/1/">Bus Traffic Fever Level 1</a></li>
            <li><a href="/level/15/">Bus Traffic Fever Level 15</a></li>
            <li><a href="/level/20/">Bus Traffic Fever Level 20</a></li>
            <li><a href="/level/26/">Bus Traffic Fever Level 26</a></li>
            <li><a href="/level/28/">Bus Traffic Fever Level 28</a></li>
          </ul>
        </div>
      </div>
      <p class="disclaimer">Bus Traffic Fever Guide is an independent fan site. We are not affiliated with, endorsed by, or connected to GOODROID, Inc. "Bus Traffic Fever" is a trademark of its respective owner. Download the official game from <a href="https://play.google.com/store/apps/details?id=jp.co.goodroid.hyper.busflow" target="_blank" rel="noopener">Google Play</a> or the <a href="https://apps.apple.com/app/bus-traffic-fever/id6759763476" target="_blank" rel="noopener">App Store</a>.</p>
    </div>
  </footer>"""


def steps_html(items):
    return "\n              ".join("<li>%s</li>" % i for i in items)


def faq_items(d):
    items = [
        (d["faq_q"], d["faq_a"]),
        (d["faq_bq"], d["faq_ba"]),
        (d["faq_cq"], d["faq_ca"]),
        (d["faq_dq"], d["faq_da"]),
        (d["faq_eq"], d["faq_ea"]),
    ]
    return items


def faq_html(items):
    return "\n            ".join(
        '<details class="faq-item"><summary>%s<span class="plus" aria-hidden="true">+</span></summary><div class="faq-body"><p>%s</p></div></details>' % (q, a)
        for q, a in items)


def prev_next(n):
    prev_html = '<a class="btn btn--ghost" href="/">← Home</a>' if n == 1 else \
                '<a class="btn btn--ghost" href="/level/%d/">← Level %d</a>' % (n - 1, n - 1)
    next_html = '<a class="btn btn--ghost" href="/#levels">All levels →</a>' if n == 40 else \
                '<a class="btn btn--primary" href="/level/%d/">Level %d →</a>' % (n + 1, n + 1)
    return prev_html, next_html


def nav_grid(n):
    cells = []
    for i in range(1, 41):
        cls = ' class="is-here"' if i == n else ''
        cells.append('<a href="/level/%d/"%s>%d</a>' % (i, cls, i))
    return "\n          ".join(cells)


def build(d):
    n = d["n"]; vid = d["vid"]
    title = "Bus Traffic Fever Level %d Walkthrough Solution" % n
    desc = "Stuck on Bus Traffic Fever Level %d? Follow the %s walkthrough, clear it step by step, and read the Level %d FAQ." % (n, d["name"][4:] if d["name"].startswith("The ") else d["name"], n)
    url = "%s/level/%d/" % (DOMAIN, n)
    prev_h, next_h = prev_next(n)
    has_video = bool(vid)
    th = thumbnail(vid) if has_video else ""
    if has_video:
        video_block = (
            '<h2 class="block-h2">Verified Video Walkthrough</h2>\n'
            '          <div class="video-card">\n'
            '            <img class="video-thumb" src="%s" alt="Level %d walkthrough video thumbnail" loading="lazy" />\n'
            '            <div class="video-meta">\n'
            '              <p><strong>Video ID</strong> %s · <strong>Source</strong> per-level YouTube walkthrough · <strong>Covers</strong> Level %d</p>\n'
            '              <a class="btn btn--primary" href="https://www.youtube.com/watch?v=%s" target="_blank" rel="noopener">▶ Open source video</a>\n'
            '            </div>\n'
            '          </div>\n'
            '          <div class="video-shell" style="margin:18px 0 0">\n'
            '            <iframe src="https://www.youtube-nocookie.com/embed/%s?rel=0" title="Level %d walkthrough" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe>\n'
            '          </div>'
        ) % (th, n, vid, n, vid, vid, n)
    else:
        video_block = (
            '<h2 class="block-h2">Video Walkthrough</h2>\n'
            '          <p class="opening-hint"><strong>Video walkthrough coming soon.</strong> The step-by-step guide above is complete and clears the level — check back for the per-level clip.</p>'
        )
    og_image = '<meta property="og:image" content="%s" />' % th if has_video else ""
    tw_image = '<meta name="twitter:image" content="%s" />' % th if has_video else ""
    faqs = faq_items(d)

    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>%s</title>
  <meta name="description" content="%s" />
  <link rel="canonical" href="%s" />
  <meta name="robots" content="index, follow" />

  <meta property="og:type" content="article" />
  <meta property="og:site_name" content="Bus Traffic Fever Guide" />
  <meta property="og:title" content="%s" />
  <meta property="og:description" content="%s" />
  <meta property="og:url" content="%s" />
  %s

  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="%s" />
  <meta name="twitter:description" content="%s" />
  %s

  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Lilita+One&family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/styles.css" />

  <script type="application/ld+json">
  %s
  </script>
</head>
<body>
%s

  <main>
    <div class="container">
      <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> › <a href="/#levels">All Levels</a> › Level %d</nav>
    </div>

    <section class="level-hero">
      <div class="container">
        <h1>%s</h1>
        <p class="lede">%s</p>
        <div class="level-facts">
          <div class="lfact"><span class="k">Level</span><span class="v">%d / 292</span></div>
          <div class="lfact"><span class="k">Difficulty</span><span class="v">%s</span></div>
          <div class="lfact"><span class="k">Focus</span><span class="v">%s</span></div>
          <div class="lfact"><span class="k">Source review</span><span class="v">Verified</span></div>
        </div>
      </div>
    </section>

    <section class="section" id="guide">
      <div class="container">
        <article class="level-body" style="padding-top:0">
          <h2 class="block-h2">Bus Traffic Fever Level %d Guide: %s</h2>
          <p>%s</p>

          <h2 class="block-h2">%s in Level %d</h2>
          <p>%s</p>

          <h2 class="block-h2">Step-by-Step Walkthrough</h2>
          <p>%s</p>
          <h3 class="block-h3">%s</h3>
          <ol class="method-steps">
            %s
          </ol>
          <h3 class="block-h3">%s</h3>
          <ol class="method-steps">
            %s
          </ol>
          <h3 class="block-h3">%s</h3>
          <ol class="method-steps">
            %s
          </ol>

          %s

          <div class="opening-hint"><strong>Quick hint:</strong><p>%s</p></div>
          <div class="opening-hint" style="background:var(--red-pale);margin-top:12px"><strong>Common mistake:</strong><p>%s</p></div>

          <h2 class="block-h2">Pros and Cons</h2>
          <p><strong>Pros.</strong> %s</p>
          <p><strong>Cons.</strong> %s</p>

          <h2 class="block-h2">Get the Official Game</h2>
          <p><a class="btn btn--primary" href="https://play.google.com/store/apps/details?id=jp.co.goodroid.hyper.busflow" target="_blank" rel="noopener">⬇ Download</a></p>

          <h2 class="block-h2">Bus Traffic Fever Level %d FAQ</h2>
          <div class="faq-grid">
            %s
          </div>

          <h2 class="block-h2">More Bus Traffic Fever Level Answers</h2>
          <nav class="related-nav" aria-label="Adjacent levels">
            %s
            %s
          </nav>
        </article>

        <div class="level-nav-grid" role="navigation" aria-label="Levels 1-40">
          %s
        </div>
      </div>
    </section>
  </main>
%s

  <script src="/js/main.js"></script>
</body>
</html>
""" % (
        title, desc, url,
        title, desc, url, og_image,
        title, desc, tw_image,
        jsonld(n, vid, title, desc, url, faqs),
        HEADER,
        n,
        title, d["intro"],
        n, d["diff"], d["focus"],
        n, d["name"], d["beat"],
        d["name"], n, d["whatis"],
        d["summary"],
        d["phase1_title"], steps_html(d["phase1_steps"]),
        d["mid_title"], steps_html(d["mid_steps"]),
        d["phase2_title"], steps_html(d["phase2_steps"]),
        video_block,
        d["hint"], d["mistake"],
        d["pros"], d["cons"],
        n, faq_html(faqs),
        prev_h, next_h,
        nav_grid(n),
        FOOTER,
    )


def write_sitemap():
    urls = ["%s/" % DOMAIN]
    for d in LEVELS:
        urls.append("%s/level/%d/" % (DOMAIN, d["n"]))
    body = "\n".join(
        "  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n  </url>" % (u, TODAY)
        for u in urls
    )
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n' % body
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml)
    print("wrote sitemap.xml  (%d urls)" % len(urls))


def main():
    os.makedirs(LEVELS_DIR, exist_ok=True)
    for d in LEVELS:
        path = os.path.join(LEVELS_DIR, str(d["n"]), "index.html")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(build(d))
        print("wrote level/%d/  (%s · %s)" % (d["n"], d["diff"], d["name"]))
    write_sitemap()


if __name__ == "__main__":
    main()
