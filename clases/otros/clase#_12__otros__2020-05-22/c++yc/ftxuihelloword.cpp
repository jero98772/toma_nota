#include <iostream>
#include <ftxui/dom/elements.hpp>
#include <ftxui/screen/screen.hpp>

int main(){
	const std::string hello={"hola"};
	ftxui::Element doc=ftxui::hbox(ftxui::text(hello)|ftxui::border);
	ftxui::Screen screen=ftxui::Screen::Create(ftxui::Domension::Fixed(hello.length()+1),ftxui::Domension::Fixed(3));
	ftxui::Render(screen,doc);
	screen.Print();
	return 0;
}