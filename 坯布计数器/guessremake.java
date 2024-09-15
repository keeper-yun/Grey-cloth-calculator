package 坯布计数器;

import java.awt.event.*;

public class guessremake implements ActionListener {
    guessMVC mvc;

    public void setguessMVC(guessMVC mvc) {
        this.mvc = mvc;
    }

    public void actionPerformed(ActionEvent e) {
        try {
            // 清空文本框内容
            mvc.text.setText("");

            // 重置 guess 对象的 sum 和 order
            mvc.guess.sum = 0.0;
            for (int i = 0; i < mvc.guess.order.length; i++) {
                mvc.guess.order[i] = 0.0;
            }

        } catch (Exception exp) {
            exp.printStackTrace();
        }
    }
}
