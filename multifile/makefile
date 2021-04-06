#comments it is used to make compilation profecc easy
#target : dependecy
#make file always executes the first target if specific target is to be executed it has to be specified
#<TAB>command
#make ## executes the first target that is project-name
#make run ## executes the "run" target
PROJECT_NAME = all.exe
SRC = test.c sum.c square.c
${PROJECT_NAME} : ${SRC}
	gcc ${SRC} -o ${PROJECT_NAME}

run : all.exe
	all.exe