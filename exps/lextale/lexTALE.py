#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on Tue Aug 22 16:08:55 2017
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('latest')

from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'lexTALE'  # from the Builder filename that created this script
expInfo = {u'proficiency': u'', u'expLang': u'en,sp', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1680, 1050), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructions_text1 = visual.TextStim(win=win, name='instructions_text1',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "practice"
practiceClock = core.Clock()
practice_text = visual.TextStim(win=win, name='practice_text',
    text='default text',
    font=u'Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);
practice_text2 = visual.TextStim(win=win, name='practice_text2',
    text='default text',
    font=u'Arial',
    pos=(0, 0.75), height=0.08, wrapWidth=None, ori=0, 
    color=u'blue', colorSpace='rgb', opacity=1,
    depth=-2.0);
practice_text_real = visual.TextStim(win=win, name='practice_text_real',
    text='default text',
    font=u'Arial',
    pos=(-0.5, -0.5), height=0.2, wrapWidth=None, ori=0, 
    color=u'green', colorSpace='rgb', opacity=1,
    depth=-3.0);
practice_text_false = visual.TextStim(win=win, name='practice_text_false',
    text='default text',
    font=u'Arial',
    pos=(0.5, -0.5), height=0.2, wrapWidth=None, ori=0, 
    color=u'red', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
msg='doh!'
feedback1_text = visual.TextStim(win=win, name='feedback1_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "check"
checkClock = core.Clock()
check_text = visual.TextStim(win=win, name='check_text',
    text=u'Any questions? \xbfPreguntas?\n\nPress the space bar to begin.\nPresiona la barra espaciadora para comenzar.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
trial_text = visual.TextStim(win=win, name='trial_text',
    text='default text',
    font=u'Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);
trial_text_real = visual.TextStim(win=win, name='trial_text_real',
    text='default text',
    font=u'Arial',
    pos=(-0.5, -0.5), height=0.2, wrapWidth=None, ori=0, 
    color=u'green', colorSpace='rgb', opacity=1,
    depth=-1.0);
trial_text_false = visual.TextStim(win=win, name='trial_text_false',
    text='default text',
    font=u'Arial',
    pos=(0.5, -0.5), height=0.2, wrapWidth=None, ori=0, 
    color=u'red', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "end"
endClock = core.Clock()
end_text = visual.TextStim(win=win, name='end_text',
    text=u'\xa1Gracias!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
instructions_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cond_files/instructions/instructions_' + expInfo['expLang'] + '.csv'),
    seed=None, name='instructions_loop')
thisExp.addLoop(instructions_loop)  # add the loop to the experiment
thisInstructions_loop = instructions_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstructions_loop.rgb)
if thisInstructions_loop != None:
    for paramName in thisInstructions_loop.keys():
        exec(paramName + '= thisInstructions_loop.' + paramName)

for thisInstructions_loop in instructions_loop:
    currentLoop = instructions_loop
    # abbreviate parameter names if possible (e.g. rgb = thisInstructions_loop.rgb)
    if thisInstructions_loop != None:
        for paramName in thisInstructions_loop.keys():
            exec(paramName + '= thisInstructions_loop.' + paramName)
    
    # ------Prepare to start Routine "instructions"-------
    t = 0
    instructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    instructions_text1.setText(instructions_text)
    instructions_key_resp_1 = event.BuilderKeyResponse()
    # keep track of which components have finished
    instructionsComponents = [instructions_text1, instructions_key_resp_1]
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instructions"-------
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_text1* updates
        if t >= 0.0 and instructions_text1.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions_text1.tStart = t
            instructions_text1.frameNStart = frameN  # exact frame index
            instructions_text1.setAutoDraw(True)
        
        # *instructions_key_resp_1* updates
        if t >= 0.0 and instructions_key_resp_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions_key_resp_1.tStart = t
            instructions_key_resp_1.frameNStart = frameN  # exact frame index
            instructions_key_resp_1.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if instructions_key_resp_1.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'instructions_loop'


# set up handler to look after randomisation of conditions etc
practice_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cond_files/trials/prac_trials_' + expInfo['expLang'] + '.csv'),
    seed=None, name='practice_trials')
thisExp.addLoop(practice_trials)  # add the loop to the experiment
thisPractice_trial = practice_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
if thisPractice_trial != None:
    for paramName in thisPractice_trial.keys():
        exec(paramName + '= thisPractice_trial.' + paramName)

for thisPractice_trial in practice_trials:
    currentLoop = practice_trials
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
    if thisPractice_trial != None:
        for paramName in thisPractice_trial.keys():
            exec(paramName + '= thisPractice_trial.' + paramName)
    
    # ------Prepare to start Routine "practice"-------
    t = 0
    practiceClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    practice_text.setText(word)
    key_resp_practice1 = event.BuilderKeyResponse()
    practice_text2.setText(prac_label)
    practice_text_real.setText(prac_button_real)
    practice_text_false.setText(prac_button_false)
    # keep track of which components have finished
    practiceComponents = [practice_text, key_resp_practice1, practice_text2, practice_text_real, practice_text_false]
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "practice"-------
    while continueRoutine:
        # get current time
        t = practiceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practice_text* updates
        if t >= 0.5 and practice_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_text.tStart = t
            practice_text.frameNStart = frameN  # exact frame index
            practice_text.setAutoDraw(True)
        
        # *key_resp_practice1* updates
        if t >= 0.5 and key_resp_practice1.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_practice1.tStart = t
            key_resp_practice1.frameNStart = frameN  # exact frame index
            key_resp_practice1.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_practice1.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_practice1.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '0'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_practice1.keys == []:  # then this was the first keypress
                    key_resp_practice1.keys = theseKeys[0]  # just the first key pressed
                    key_resp_practice1.rt = key_resp_practice1.clock.getTime()
                    # was this 'correct'?
                    if (key_resp_practice1.keys == str(correct_response)) or (key_resp_practice1.keys == correct_response):
                        key_resp_practice1.corr = 1
                    else:
                        key_resp_practice1.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *practice_text2* updates
        if t >= 0.5 and practice_text2.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_text2.tStart = t
            practice_text2.frameNStart = frameN  # exact frame index
            practice_text2.setAutoDraw(True)
        
        # *practice_text_real* updates
        if t >= 0.5 and practice_text_real.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_text_real.tStart = t
            practice_text_real.frameNStart = frameN  # exact frame index
            practice_text_real.setAutoDraw(True)
        
        # *practice_text_false* updates
        if t >= 0.5 and practice_text_false.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_text_false.tStart = t
            practice_text_false.frameNStart = frameN  # exact frame index
            practice_text_false.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice"-------
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_practice1.keys in ['', [], None]:  # No response was made
        key_resp_practice1.keys=None
        # was no response the correct answer?!
        if str(correct_response).lower() == 'none':
           key_resp_practice1.corr = 1  # correct non-response
        else:
           key_resp_practice1.corr = 0  # failed to respond (incorrectly)
    # store data for practice_trials (TrialHandler)
    practice_trials.addData('key_resp_practice1.keys',key_resp_practice1.keys)
    practice_trials.addData('key_resp_practice1.corr', key_resp_practice1.corr)
    if key_resp_practice1.keys != None:  # we had a response
        practice_trials.addData('key_resp_practice1.rt', key_resp_practice1.rt)
    # the Routine "practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if not key_resp_practice1.keys: 
        msg="Failed to resond"
    elif key_resp_practice1.corr: 
        msg="Correcto!"
    else: 
        msg="Ooo! Wrong! Te has equivocado!"
    key_resp_feedback1 = event.BuilderKeyResponse()
    feedback1_text.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [key_resp_feedback1, feedback1_text]
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *key_resp_feedback1* updates
        if t >= 0.0 and key_resp_feedback1.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_feedback1.tStart = t
            key_resp_feedback1.frameNStart = frameN  # exact frame index
            key_resp_feedback1.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_feedback1.status == STARTED and t >= frameRemains:
            key_resp_feedback1.status = STOPPED
        if key_resp_feedback1.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *feedback1_text* updates
        if t >= 0.0 and feedback1_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback1_text.tStart = t
            feedback1_text.frameNStart = frameN  # exact frame index
            feedback1_text.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if feedback1_text.status == STARTED and t >= frameRemains:
            feedback1_text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'practice_trials'


# ------Prepare to start Routine "check"-------
t = 0
checkClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_check = event.BuilderKeyResponse()
# keep track of which components have finished
checkComponents = [check_text, key_resp_check]
for thisComponent in checkComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "check"-------
while continueRoutine:
    # get current time
    t = checkClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *check_text* updates
    if t >= 0.0 and check_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        check_text.tStart = t
        check_text.frameNStart = frameN  # exact frame index
        check_text.setAutoDraw(True)
    
    # *key_resp_check* updates
    if t >= 0.5 and key_resp_check.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_check.tStart = t
        key_resp_check.frameNStart = frameN  # exact frame index
        key_resp_check.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_check.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in checkComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "check"-------
for thisComponent in checkComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "check" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cond_files/trials/trials_' + expInfo['expLang'] + '.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    trial_text.setText(word)
    trial_text_real.setText(button_real)
    trial_text_false.setText(button_false)
    key_resp_trial = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [trial_text, trial_text_real, trial_text_false, key_resp_trial]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial_text* updates
        if t >= 0.5 and trial_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_text.tStart = t
            trial_text.frameNStart = frameN  # exact frame index
            trial_text.setAutoDraw(True)
        
        # *trial_text_real* updates
        if t >= 0.25 and trial_text_real.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_text_real.tStart = t
            trial_text_real.frameNStart = frameN  # exact frame index
            trial_text_real.setAutoDraw(True)
        
        # *trial_text_false* updates
        if t >= 0.25 and trial_text_false.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_text_false.tStart = t
            trial_text_false.frameNStart = frameN  # exact frame index
            trial_text_false.setAutoDraw(True)
        
        # *key_resp_trial* updates
        if t >= 0.5 and key_resp_trial.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_trial.tStart = t
            key_resp_trial.frameNStart = frameN  # exact frame index
            key_resp_trial.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_trial.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_trial.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '0'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_trial.keys == []:  # then this was the first keypress
                    key_resp_trial.keys = theseKeys[0]  # just the first key pressed
                    key_resp_trial.rt = key_resp_trial.clock.getTime()
                    # was this 'correct'?
                    if (key_resp_trial.keys == str(correct_response)) or (key_resp_trial.keys == correct_response):
                        key_resp_trial.corr = 1
                    else:
                        key_resp_trial.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_trial.keys in ['', [], None]:  # No response was made
        key_resp_trial.keys=None
        # was no response the correct answer?!
        if str(correct_response).lower() == 'none':
           key_resp_trial.corr = 1  # correct non-response
        else:
           key_resp_trial.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_trial.keys',key_resp_trial.keys)
    trials.addData('key_resp_trial.corr', key_resp_trial.corr)
    if key_resp_trial.keys != None:  # we had a response
        trials.addData('key_resp_trial.rt', key_resp_trial.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
key_resp_end = event.BuilderKeyResponse()
# keep track of which components have finished
endComponents = [end_text, key_resp_end]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if t >= 0.0 and end_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_text.tStart = t
        end_text.frameNStart = frameN  # exact frame index
        end_text.setAutoDraw(True)
    frameRemains = 0.0 + 5.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if end_text.status == STARTED and t >= frameRemains:
        end_text.setAutoDraw(False)
    
    # *key_resp_end* updates
    if t >= 0.0 and key_resp_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_end.tStart = t
        key_resp_end.frameNStart = frameN  # exact frame index
        key_resp_end.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    frameRemains = 0.0 + 5.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if key_resp_end.status == STARTED and t >= frameRemains:
        key_resp_end.status = STOPPED
    if key_resp_end.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
