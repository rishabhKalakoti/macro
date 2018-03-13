extern printf
extern atoi
SECTION .data
forS db '%d',10,0
SECTION .bss
e resb 64
o resb 64
SECTION .text
global main
main:
mov rax,0
mov [e],rax
mov rax,0
mov [o],rax
mov r8,8
mov rcx,rdi
mov rbx, qword[rsi+r8]
mov rcx,0
mov rdx,rbx
loop:
cmp byte[rdx+rcx],0
je end
cmp byte[rdx+rcx],'0'
je even
cmp byte[rdx+rcx],'2'
je even
cmp byte[rdx+rcx],'4'
je even
cmp byte[rdx+rcx],'6'
je even
cmp byte[rdx+rcx],'8'
je even
jmp odd
even:
mov eax,[e]
inc eax
mov [e],eax
call next
odd:
mov eax,[o]
inc eax
mov [o],eax
next:
inc rcx
jmp loop

end:
push rdi
push rsi
mov rdi,forS
mov rsi,[e]
mov rax,0
call printf
pop rsi
pop rdi

push rdi
push rsi
mov rdi,forS
mov rsi,[o]
mov rax,0
call printf
pop rsi
pop rdi


mov eax,1
mov ebx,0
int 80h
