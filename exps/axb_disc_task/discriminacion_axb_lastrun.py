#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Wed Nov  3 14:47:51 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'discrimination_axb'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/kyleparrish/Documents/GitHub/dissertation_parrish/exps/axb_disc_task/discriminacion_axb_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1.000,1.000,1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
insructions = visual.TextStim(win=win, name='insructions',
    text='Listen to the following sequences of sounds. \n\nYour task is to determine if one of the sounds is different.\n\nIf the first sound is different press 1. If the third sound is different press 0. If they are the same press the space bar.\n\nRespond as quickly as possible without making mistakes. \n\nPress the space bar to begin. ',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_ins = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
sound_stim1 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_stim1')
sound_stim1.setVolume(1)
sound_stim2 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_stim2')
sound_stim2.setVolume(1)
sound_stim3 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_stim3')
sound_stim3.setVolume(1)
text_response_first = visual.TextStim(win=win, name='text_response_first',
    text='First is different',
    font='Arial',
    pos=[-0.5, 0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_response_third = visual.TextStim(win=win, name='text_response_third',
    text='Third is different',
    font='Arial',
    pos=[0.5, 0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_response_same = visual.TextStim(win=win, name='text_response_same',
    text='They are the same',
    font='Arial',
    pos=(0, -0.5), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
key_resp_trial = keyboard.Keyboard()
text_trial_cross = visual.TextStim(win=win, name='text_trial_cross',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "end"
endClock = core.Clock()
text_end = visual.TextStim(win=win, name='text_end',
    text='Thank you.',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_end = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_ins.keys = []
key_resp_ins.rt = []
_key_resp_ins_allKeys = []
# keep track of which components have finished
instructionsComponents = [insructions, key_resp_ins]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *insructions* updates
    if insructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        insructions.frameNStart = frameN  # exact frame index
        insructions.tStart = t  # local t and not account for scr refresh
        insructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(insructions, 'tStartRefresh')  # time at next scr refresh
        insructions.setAutoDraw(True)
    
    # *key_resp_ins* updates
    if key_resp_ins.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_ins.frameNStart = frameN  # exact frame index
        key_resp_ins.tStart = t  # local t and not account for scr refresh
        key_resp_ins.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_ins, 'tStartRefresh')  # time at next scr refresh
        key_resp_ins.status = STARTED
        # keyboard checking is just starting
        key_resp_ins.clock.reset()  # now t=0
    if key_resp_ins.status == STARTED:
        theseKeys = key_resp_ins.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_ins_allKeys.extend(theseKeys)
        if len(_key_resp_ins_allKeys):
            key_resp_ins.keys = _key_resp_ins_allKeys[-1].name  # just the last key pressed
            key_resp_ins.rt = _key_resp_ins_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('insructions.started', insructions.tStartRefresh)
thisExp.addData('insructions.stopped', insructions.tStopRefresh)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_file/trials.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(4.750000)
    # update component parameters for each repeat
    sound_stim1.setSound(stim1, secs=0.25, hamming=True)
    sound_stim1.setVolume(1, log=False)
    sound_stim2.setSound(stim2, secs=0.25, hamming=True)
    sound_stim2.setVolume(1, log=False)
    sound_stim3.setSound(stim3, secs=0.25, hamming=True)
    sound_stim3.setVolume(1, log=False)
    key_resp_trial.keys = []
    key_resp_trial.rt = []
    _key_resp_trial_allKeys = []
    # keep track of which components have finished
    trialComponents = [sound_stim1, sound_stim2, sound_stim3, text_response_first, text_response_third, text_response_same, key_resp_trial, text_trial_cross]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_stim1
        if sound_stim1.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
            # keep track of start time/frame for later
            sound_stim1.frameNStart = frameN  # exact frame index
            sound_stim1.tStart = t  # local t and not account for scr refresh
            sound_stim1.tStartRefresh = tThisFlipGlobal  # on global time
            sound_stim1.play(when=win)  # sync with win flip
        if sound_stim1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_stim1.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_stim1.tStop = t  # not accounting for scr refresh
                sound_stim1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_stim1, 'tStopRefresh')  # time at next scr refresh
                sound_stim1.stop()
        # start/stop sound_stim2
        if sound_stim2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            sound_stim2.frameNStart = frameN  # exact frame index
            sound_stim2.tStart = t  # local t and not account for scr refresh
            sound_stim2.tStartRefresh = tThisFlipGlobal  # on global time
            sound_stim2.play(when=win)  # sync with win flip
        if sound_stim2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_stim2.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_stim2.tStop = t  # not accounting for scr refresh
                sound_stim2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_stim2, 'tStopRefresh')  # time at next scr refresh
                sound_stim2.stop()
        # start/stop sound_stim3
        if sound_stim3.status == NOT_STARTED and tThisFlip >= 1.75-frameTolerance:
            # keep track of start time/frame for later
            sound_stim3.frameNStart = frameN  # exact frame index
            sound_stim3.tStart = t  # local t and not account for scr refresh
            sound_stim3.tStartRefresh = tThisFlipGlobal  # on global time
            sound_stim3.play(when=win)  # sync with win flip
        if sound_stim3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_stim3.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_stim3.tStop = t  # not accounting for scr refresh
                sound_stim3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_stim3, 'tStopRefresh')  # time at next scr refresh
                sound_stim3.stop()
        
        # *text_response_first* updates
        if text_response_first.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            text_response_first.frameNStart = frameN  # exact frame index
            text_response_first.tStart = t  # local t and not account for scr refresh
            text_response_first.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_response_first, 'tStartRefresh')  # time at next scr refresh
            text_response_first.setAutoDraw(True)
        if text_response_first.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_response_first.tStartRefresh + 2.75-frameTolerance:
                # keep track of stop time/frame for later
                text_response_first.tStop = t  # not accounting for scr refresh
                text_response_first.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_response_first, 'tStopRefresh')  # time at next scr refresh
                text_response_first.setAutoDraw(False)
        
        # *text_response_third* updates
        if text_response_third.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            text_response_third.frameNStart = frameN  # exact frame index
            text_response_third.tStart = t  # local t and not account for scr refresh
            text_response_third.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_response_third, 'tStartRefresh')  # time at next scr refresh
            text_response_third.setAutoDraw(True)
        if text_response_third.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_response_third.tStartRefresh + 2.75-frameTolerance:
                # keep track of stop time/frame for later
                text_response_third.tStop = t  # not accounting for scr refresh
                text_response_third.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_response_third, 'tStopRefresh')  # time at next scr refresh
                text_response_third.setAutoDraw(False)
        
        # *text_response_same* updates
        if text_response_same.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            text_response_same.frameNStart = frameN  # exact frame index
            text_response_same.tStart = t  # local t and not account for scr refresh
            text_response_same.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_response_same, 'tStartRefresh')  # time at next scr refresh
            text_response_same.setAutoDraw(True)
        if text_response_same.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_response_same.tStartRefresh + 2.75-frameTolerance:
                # keep track of stop time/frame for later
                text_response_same.tStop = t  # not accounting for scr refresh
                text_response_same.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_response_same, 'tStopRefresh')  # time at next scr refresh
                text_response_same.setAutoDraw(False)
        
        # *key_resp_trial* updates
        waitOnFlip = False
        if key_resp_trial.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_trial.frameNStart = frameN  # exact frame index
            key_resp_trial.tStart = t  # local t and not account for scr refresh
            key_resp_trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_trial, 'tStartRefresh')  # time at next scr refresh
            key_resp_trial.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_trial.clock.reset)  # t=0 on next screen flip
        if key_resp_trial.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_trial.tStartRefresh + 2.75-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_trial.tStop = t  # not accounting for scr refresh
                key_resp_trial.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_trial, 'tStopRefresh')  # time at next scr refresh
                key_resp_trial.status = FINISHED
        if key_resp_trial.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_trial.getKeys(keyList=['1', '0', 'space'], waitRelease=False)
            _key_resp_trial_allKeys.extend(theseKeys)
            if len(_key_resp_trial_allKeys):
                key_resp_trial.keys = _key_resp_trial_allKeys[0].name  # just the first key pressed
                key_resp_trial.rt = _key_resp_trial_allKeys[0].rt
                # was this correct?
                if (key_resp_trial.keys == str(isCorrect)) or (key_resp_trial.keys == isCorrect):
                    key_resp_trial.corr = 1
                else:
                    key_resp_trial.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *text_trial_cross* updates
        if text_trial_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_trial_cross.frameNStart = frameN  # exact frame index
            text_trial_cross.tStart = t  # local t and not account for scr refresh
            text_trial_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_trial_cross, 'tStartRefresh')  # time at next scr refresh
            text_trial_cross.setAutoDraw(True)
        if text_trial_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_trial_cross.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                text_trial_cross.tStop = t  # not accounting for scr refresh
                text_trial_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_trial_cross, 'tStopRefresh')  # time at next scr refresh
                text_trial_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_stim1.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_stim1.started', sound_stim1.tStartRefresh)
    trials.addData('sound_stim1.stopped', sound_stim1.tStopRefresh)
    sound_stim2.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_stim2.started', sound_stim2.tStartRefresh)
    trials.addData('sound_stim2.stopped', sound_stim2.tStopRefresh)
    sound_stim3.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_stim3.started', sound_stim3.tStartRefresh)
    trials.addData('sound_stim3.stopped', sound_stim3.tStopRefresh)
    trials.addData('text_response_first.started', text_response_first.tStartRefresh)
    trials.addData('text_response_first.stopped', text_response_first.tStopRefresh)
    trials.addData('text_response_third.started', text_response_third.tStartRefresh)
    trials.addData('text_response_third.stopped', text_response_third.tStopRefresh)
    trials.addData('text_response_same.started', text_response_same.tStartRefresh)
    trials.addData('text_response_same.stopped', text_response_same.tStopRefresh)
    # check responses
    if key_resp_trial.keys in ['', [], None]:  # No response was made
        key_resp_trial.keys = None
        # was no response the correct answer?!
        if str(isCorrect).lower() == 'none':
           key_resp_trial.corr = 1;  # correct non-response
        else:
           key_resp_trial.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_trial.keys',key_resp_trial.keys)
    trials.addData('key_resp_trial.corr', key_resp_trial.corr)
    if key_resp_trial.keys != None:  # we had a response
        trials.addData('key_resp_trial.rt', key_resp_trial.rt)
    trials.addData('key_resp_trial.started', key_resp_trial.tStartRefresh)
    trials.addData('key_resp_trial.stopped', key_resp_trial.tStopRefresh)
    trials.addData('text_trial_cross.started', text_trial_cross.tStartRefresh)
    trials.addData('text_trial_cross.stopped', text_trial_cross.tStopRefresh)
    thisExp.nextEntry()
    
# completed 3 repeats of 'trials'


# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_end.keys = []
key_resp_end.rt = []
_key_resp_end_allKeys = []
# keep track of which components have finished
endComponents = [text_end, key_resp_end]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_end* updates
    if text_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_end.frameNStart = frameN  # exact frame index
        text_end.tStart = t  # local t and not account for scr refresh
        text_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_end, 'tStartRefresh')  # time at next scr refresh
        text_end.setAutoDraw(True)
    if text_end.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_end.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            text_end.tStop = t  # not accounting for scr refresh
            text_end.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_end, 'tStopRefresh')  # time at next scr refresh
            text_end.setAutoDraw(False)
    
    # *key_resp_end* updates
    waitOnFlip = False
    if key_resp_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_end.frameNStart = frameN  # exact frame index
        key_resp_end.tStart = t  # local t and not account for scr refresh
        key_resp_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_end, 'tStartRefresh')  # time at next scr refresh
        key_resp_end.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_end.clock.reset)  # t=0 on next screen flip
    if key_resp_end.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_end.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_end_allKeys.extend(theseKeys)
        if len(_key_resp_end_allKeys):
            key_resp_end.keys = _key_resp_end_allKeys[-1].name  # just the last key pressed
            key_resp_end.rt = _key_resp_end_allKeys[-1].rt
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_end.started', text_end.tStartRefresh)
thisExp.addData('text_end.stopped', text_end.tStopRefresh)
# check responses
if key_resp_end.keys in ['', [], None]:  # No response was made
    key_resp_end.keys = None
thisExp.addData('key_resp_end.keys',key_resp_end.keys)
if key_resp_end.keys != None:  # we had a response
    thisExp.addData('key_resp_end.rt', key_resp_end.rt)
thisExp.addData('key_resp_end.started', key_resp_end.tStartRefresh)
thisExp.addData('key_resp_end.stopped', key_resp_end.tStopRefresh)
thisExp.nextEntry()
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
