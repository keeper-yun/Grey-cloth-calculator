package 坯布计数器;

import java.awt.event.*;
import java.util.Scanner;

public class guessremake implements ActionListener{
    guessMVC mvc;

    public void setguessMVC(guessMVC mvc){
        this.mvc =mvc;
    }
    public void actionPerformed(ActionEvent e) {

        try {

            mvc.text.setText("");

        } catch (Exception exp) {
            exp.printStackTrace();
        }
    }
}
