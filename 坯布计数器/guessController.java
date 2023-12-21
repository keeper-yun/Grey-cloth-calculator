package 坯布计数器;

import java.awt.event.*;
import java.util.Scanner;

import 坯布计数器.guessMVC;

public class guessController implements ActionListener {
    guessMVC mvc;
    
    public void setguessMVC(guessMVC mvc){
        this.mvc =mvc;
    }
    
    public void actionPerformed(ActionEvent e) {
        try {
            Scanner scanner = new Scanner(mvc.text.getText());
            scanner.useDelimiter("[^0123456789.]+");

            int i = 1; // 用于索引数组
            while (scanner.hasNext()) {
                double number = scanner.nextDouble();
                mvc.guess.order[i] = number;
                mvc.guess.sum += number;
                i++;
            }

            mvc.text.setText(mvc.guess.toString());
            mvc.guess.sum = 0;

        } catch (Exception exp) {
            exp.printStackTrace();
        }
    }
}


