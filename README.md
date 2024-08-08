# What is this?
This is a Vim function that is used for fast creation of a verilog module instantiation template. Some other functionality would be cool, such as:
- State Machine Template Generator
- Basic Module template

# What can it do?
Currently the feature set is small, but here is what it can do
- Make a instantiation template from a file that is in the same directory
- template fully supports parameters and port lists as well as comments for them

# How to use
1. Simply add this function and map to .vimrc
```
" verilogThings Template Generator
nnoremap <C-e>t :call GetArgument()<CR> " can change key binds here
" function to place template in your a buffer
function! GetArgument()
	let l:word = expand('<cword>')
	let l:command = 'bash /path/to/repo/verilogThings/getModuleTemplate.sh ' . shellescape(l:word)
	let l:output = system(l:command)
	let @a = l:output
endfunction
```
2. Ensure the python script and shell script are both executable
```
chmod +x /path/to/repo/verilogThings/getModuleTemplate.sh
chmod +x /path/to/repo/verilogThings/getModuleTemplate.py
```

# What do I want it to do?
These are just a few features that would make this a more useful tool in a real workflow
- Look at a broader set of files starting from a given directory 
- Ignores single line comments above the module \<module_name\> verilog construct that start at the beginning of the line
- More if anyone thinks of anything


