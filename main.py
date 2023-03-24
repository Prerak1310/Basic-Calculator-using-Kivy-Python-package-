from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
class CalculatorApp(App):
    def build(self):
        box_structure=BoxLayout(orientation='vertical')
        output_text=Label(size_hint_y=0.75,font_size=50)
        button_symbols=('1', '2', '3', '+',
                          '4', '5', '6', '-',
                          '7', '8', '9', '.',
                          '0', '*', '/', '=')
        button_grid=GridLayout(cols=4,size_hint_y=2)        
        for symbols in button_symbols:
            button_grid.add_widget(Button(text=symbols))
        clear_button=Button(text="Clear",size_hint_y=None, height=100)
        def print_output(instance):
            output_text.text=output_text.text+instance.text
        for button in button_grid.children[1:]:
            button.bind(on_press=print_output)
        def clear_label(instance):
            output_text.text=" "
        clear_button.bind(on_press=clear_label)      
        def calc_result(instance):
            try:
                output_text.text=str(eval(output_text.text)) 
            except SyntaxError:
                output_text.text="Syntax Error"
        button_grid.children[0].bind(on_press=calc_result)
        box_structure.add_widget(output_text)
        box_structure.add_widget(button_grid)
        box_structure.add_widget(clear_button)
        return box_structure

if __name__=='__main__':
    CalculatorApp().run()
