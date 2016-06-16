% DESCRIPTION
% For today's challenge we will be focusing on generating a serieses waveforms
% at specific frequencies, known as musical notes. Ideally you would be able
% to push these frequencies directly to your speakers, but this can be difficult
% depending on your operating system.
% For Linux systems with ALSA, you can use the aplay utility.
% ./solution | aplay -f U8 -r 8000
% For other systems you can use Audacity, which features a raw data import utility.
% 
%
% INPUT DESCRIPTION
% You will be given a sample rate in Hz (bytes per second), followed by a 
% duration for each note (milliseconds), and then finally a string of notes
% represented as the letters A through G (and _ for rest).
%
% CHALLENGE INPUT
% 8000
% 300
% ABCDEFG_GFEDCBA
% 
%
% OUTPUT DESCRIPTION
% You should output a string of bytes (unsigned 8 bit integers) either as a
% binary stream, or to a binary file. These bytes should represent the 
% waveforms for the frequencies of the notes.
%
% CHALLENGE OUTPUT
% Since the output will be a string of 36000 bytes, it is provided below as
% a download. Note that it does not have to output exactly these bytes, but
% it must be the same notes when played.
% You can listen to the data either by playing it straight with aplay, which
% should pick up on the format automatically, or by piping to aplay and 
% specifying the format, or by importing into audacity and playing from there.
% DOWNLOAD: https://raw.githubusercontent.com/G33kDude/DailyProgrammer/master/%5B2016-06-15%5D%20Challenge%20%23271%20%5BIntermediate%5D%20Making%20Waves/out.wav

function y = making_waves(Fs, note_duration, notes)
note_duration_seconds = note_duration/1000;
note_length = note_duration_seconds*Fs;

%Saving space in memory for the result
y = zeros(1, length(notes)*note_length);

%Generating the time scale. It will be the same for each note, so we'll
%only generate it once.
t_note = 0:1/Fs:note_duration_seconds;

%Generating the waveform for each note
for i = 1:length(notes)
    f = get_frequency(notes(i));

    y_note = sin(2*pi*f*t_note);
    y((i-1)*note_length + 1 : i*note_length) = y_note(1:end-1);

end

end


function f = get_frequency(note)

    switch(note)
        case 'A'
            f = 440;
        case 'B'
            f = 493.88;
        case 'C'
            f = 523.25;
        case 'D'
            f = 587.33;
        case 'E'
            f = 659.25;
        case 'F'
            f = 698.46;
        case 'G'
            f = 783.99;
        case '_'
            f = 0;
    end
end