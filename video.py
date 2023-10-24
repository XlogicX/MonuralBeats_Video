import curses
import re
import time

def bass_drum(stdscr):
	line_attrs = []
	with open('bd.txt','r') as BD:
		for idx,line in enumerate(BD):
			line_attrs = line.split(',')
			stdscr.addstr(int(line_attrs[0]),int(line_attrs[1]), ''.join(line_attrs[2:]).strip(), curses.color_pair(1))
	stdscr.refresh()

def set_clear(stdscr):
	with open('drumset.txt','r') as DRUM:
		for idx,line in enumerate(DRUM):
			stdscr.addstr(idx, 0, line)
	stdscr.refresh()

def main(stdscr):
	# Clear screen
	stdscr.clear()

	# Init the Screen dimensions
	begin_x = 0; begin_y = 0
	height = 64; width = 184
	win = curses.newwin(height, width, begin_y, begin_x)

	# Display Black and White Drumset
	with open('drumset.txt','r') as DRUM:
		for idx,line in enumerate(DRUM):
			stdscr.addstr(idx, 0, line)
	stdscr.refresh()	
	#curses.wrapper(set_clear)

	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
	curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
	curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
	curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_RED)

	DRUM = open("drumset.txt", "r") 
	data = DRUM.read() 
	drumset = data.split("\n") 
	DRUM.close()

	BD = open("bd.txt", "r") 
	data = BD.read() 
	bdkit = data.split("\n") 
	BD.close()

	SN = open("snare.txt", "r") 
	data = SN.read() 
	snarekit = data.split("\n") 
	SN.close()	

	HC = open("hat_closed.txt", "r") 
	data = HC.read() 
	hckit = data.split("\n") 
	HC.close()	

	HO = open("hat_open.txt", "r") 
	data = HO.read() 
	hokit = data.split("\n") 
	HO.close()

	TH = open("tom_hi.txt", "r") 
	data = TH.read() 
	thkit = data.split("\n") 
	TH.close()		

	TM = open("tom_med.txt", "r") 
	data = TM.read() 
	tmkit = data.split("\n") 
	TM.close()	

	TL = open("tom_lo.txt", "r") 
	data = TL.read() 
	tlkit = data.split("\n") 
	TL.close()			

	with open('log.txt','r') as TEH_DRUMS:
		line_attrs = []
		start = time.clock_gettime(time.CLOCK_REALTIME)
		for hit in TEH_DRUMS:
			if 'flac' in hit:
				matches = re.match(r'time: (\d+\.\d+) - "(.+?)\.flac"',hit)
				tstamp = float(matches.group(1))
				drum = matches.group(2)

				if 'bd_' in drum: 
					bd_idx = ['bd_tek','bd_ada','bd_boom','bd_zum','bd_fat','bd_klub','bd_sone']
					for idx,drm in enumerate(bd_idx):
						if drm in drum:
							dcolor = idx + 1
					for idx,line in enumerate(bdkit):
						line_attrs = line.split(',')
						stdscr.addstr(int(line_attrs[0]),int(line_attrs[1]), ''.join(line_attrs[2:]).strip(), curses.color_pair(dcolor))
					stdscr.refresh()
					if tstamp > 0: time.sleep(start + tstamp - time.clock_gettime(time.CLOCK_REALTIME))
					for idx,line in enumerate(drumset):
						stdscr.addstr(idx, 0, line)					

				elif 'snare' in drum or 'sn_' in drum:
					sn_idx = ['drum_snare_hard.flac','drum_snare_soft.flac','elec_hi_snare.flac','sn_zome','sn_generic']
					for idx,drm in enumerate(sn_idx):
						if drm in drum:
							dcolor = idx + 1
					for idx,line in enumerate(snarekit):
						line_attrs = line.split(',')
						stdscr.addstr(int(line_attrs[0]),int(line_attrs[1]), ''.join(line_attrs[2:]).strip(), curses.color_pair(dcolor))
					stdscr.refresh()
					if tstamp > 0: time.sleep(start + tstamp - time.clock_gettime(time.CLOCK_REALTIME))
					for idx,line in enumerate(drumset):
						stdscr.addstr(idx, 0, line)

				elif 'cymbal_closed' in drum or 'cymbal_soft' in drum or 'elec_tick' in drum:
					hc_idx = ['drum_cymbal_closed', 'drum_cymbal_soft', 'elec_tick']
					for idx,drm in enumerate(hc_idx):
						if drm in drum:
							dcolor = idx + 1
					for idx,line in enumerate(hckit):
						line_attrs = line.split(',')
						stdscr.addstr(int(line_attrs[0]),int(line_attrs[1]), ''.join(line_attrs[2:]).strip(), curses.color_pair(dcolor))
					stdscr.refresh()
					if tstamp > 0: time.sleep(start + tstamp - time.clock_gettime(time.CLOCK_REALTIME))
					for idx,line in enumerate(drumset):
						stdscr.addstr(idx, 0, line)

				elif 'cymbal_pedal' in drum or 'cymbal_open' in drum or 'perc_swash' in drum or 'drum_splash' in drum:
					ho_idx = ['cymbal_pedal', 'cymbal_open', 'perc_swash', 'drum_splash']
					for idx,drm in enumerate(ho_idx):
						if drm in drum:
							dcolor = idx + 1
					for idx,line in enumerate(hokit):
						line_attrs = line.split(',')
						stdscr.addstr(int(line_attrs[0]),int(line_attrs[1]), ''.join(line_attrs[2:]).strip(), curses.color_pair(dcolor))
					stdscr.refresh()
					if tstamp > 0: time.sleep(start + tstamp - time.clock_gettime(time.CLOCK_REALTIME))
					for idx,line in enumerate(drumset):
						stdscr.addstr(idx, 0, line)

				elif 'drum_tom_hi_soft' in drum:
					for idx,line in enumerate(thkit):
						line_attrs = line.split(',')
						stdscr.addstr(int(line_attrs[0]),int(line_attrs[1]), ''.join(line_attrs[2:]).strip(), curses.color_pair(6))
					stdscr.refresh()
					if tstamp > 0: time.sleep(start + tstamp - time.clock_gettime(time.CLOCK_REALTIME))
					for idx,line in enumerate(drumset):
						stdscr.addstr(idx, 0, line)

				elif 'drum_tom_mid_soft' in drum:
					for idx,line in enumerate(tmkit):
						line_attrs = line.split(',')
						stdscr.addstr(int(line_attrs[0]),int(line_attrs[1]), ''.join(line_attrs[2:]).strip(), curses.color_pair(5))
					stdscr.refresh()
					if tstamp > 0: time.sleep(start + tstamp - time.clock_gettime(time.CLOCK_REALTIME))
					for idx,line in enumerate(drumset):
						stdscr.addstr(idx, 0, line)

				elif 'drum_tom_lo_soft' in drum or 'elec_fuzz_tom' in drum:
					tl_idx = ['drum_tom_lo_soft', 'elec_fuzz_tom']
					for idx,drm in enumerate(tl_idx):
						if drm in drum:
							dcolor = idx + 6					
					for idx,line in enumerate(tlkit):
						line_attrs = line.split(',')
						stdscr.addstr(int(line_attrs[0]),int(line_attrs[1]), ''.join(line_attrs[2:]).strip(), curses.color_pair(dcolor))
					stdscr.refresh()
					if tstamp > 0: time.sleep(start + tstamp - time.clock_gettime(time.CLOCK_REALTIME))
					for idx,line in enumerate(drumset):
						stdscr.addstr(idx, 0, line)

				else:
					stdscr.addstr(1,1,"PATTERN: {}".format(hit),curses.colorpair(1))
					stdscr.getkey()

					stdscr.refresh()
				

curses.wrapper(main)

#  0:black, 1:red, 2:green, 3:yellow, 4:blue, 5:magenta, 6:cyan, and 7:white
