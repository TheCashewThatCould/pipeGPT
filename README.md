```bash
git clone https://github.com/TheCashewThatCould/pipeGPT.git
export PATH="$PATH:$(pwd)"
```
examples
```bash
echo "how is your day" | GPT
```
echos to GPT and prints response
```bash
python main.py |& GPT
```
sends to GPT output and error message
```bash
GPT -f main.py
```
sends file
```bash
GPT -f main.py -w
```
rewrites file in main.py.gpt
```bash
GPT -f main.py -a
```
appends output to main.py
```bash
python main.py | GPT -e
```
explains the cause of an error message

these examples can be combined together with the exception of -e, -w, and -a
