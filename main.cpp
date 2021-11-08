#include <iostream>
#include <fstream>
#include <string>
#include <stdbool.h>
#include <typeinfo>

 /* TODO
 * error handling
 * website opening
 */

int main(int argc, const char *argv[])
{
	if (argc == 3)
	{
        std::string appFile{argv[1]}, name{argv[2]};
		// apps and files TODO(websites) are opened differently
		if (appFile == "a")
		{
            // debugging line
			//std::cout << "app detected, name: " << name << std::endl;

			// get open program command name as const char*
			const char* ccProgram = name.c_str();
	
			// debugging line
			//std::cout << "Launching " << name << std::endl;
			
			// execute command
			system(ccProgram);
		}

		if (appFile == "f")
		{
			// debugging line
            //std::cout << "file detected, name: " << name << std::endl;

			// find and save the path of the file
			// get the find command as str
			std::string strCommand{ "find ~/ -iname " };
			strCommand.append(name);

			// get the save command as str
			strCommand.append(" >> temp.txt");
			
			// debugging line
			//std::cout << "string: " << strCommand << std::endl;
			
			// get full find command as const char*
			const char* ccCommand = strCommand.c_str();
			
			// debugging line
			//std::cout << "const char: " << ccCommand << std::endl;

			// execute find and save command
			system(ccCommand);
			
			// create variables for reading temp.txt
			std::string text{};
			std::string targetPath{};
			
			// open and read file
			std::ifstream readfile("temp.txt");
			//system("ls");
			if (readfile.is_open())
			{
				//std::cout << "readfile.is_open()" << std::endl;
				while (std::getline(readfile, text))
				{
					targetPath = text;
					//std::cout << text << std::endl;
					//std::cout << "reading..." << std::endl;
				}
			}
			else std::cout << "unable to open file" << std::endl;
			readfile.close();

			// debugging line
			//std::cout << "found path: " << targetPath << std::endl;
			
			// get file path and delete temp.txt
			//std::string targetPath{ getContents("temp.txt") };
			remove("temp.txt");
			
			// execute open command
			std::string openCommand{ "xdg-open " };
			openCommand.append(targetPath);
			system(openCommand.c_str());
		}
	}
	// if inputs are bad TODO: beef up
	else
	{
		std::cout << "argc != 2" << std::endl;
        std::cout << "improper arguments, usage: \n ./spSearcher <a,f> <app/file name>" << std::endl;
	}
	return 0;
}
