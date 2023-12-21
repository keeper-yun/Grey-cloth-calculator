package 坯布计数器;

import java.awt.*;
import java.awt.event.ActionListener;

import javax.swing.*;

public class guessMVC extends JFrame {

    guess guess = new guess();

    JButton submit,remake;
    JLabel label1;
    JTextArea text;
    Box basebox, box1, box2,boxfirst;

    guessController controller = new guessController();
    guessremake controller2 = new guessremake();

    guessMVC() {
        setLayout(new java.awt.FlowLayout());
        init();
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    void init() {
        label1 = new JLabel("请在方框中输入多卷坯布的长度");
        Font currentFont = label1.getFont();
        Font newFont = currentFont.deriveFont((float)20.0);
        label1.setFont(newFont);
        
        submit = new JButton("提交");
        remake = new JButton("重置");

        text = new JTextArea(10, 10);

        // 使用JScrollPane包装JTextArea
        JScrollPane scrollPane = new JScrollPane(text);
        scrollPane.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);

        basebox = Box.createVerticalBox();
        box1 = Box.createVerticalBox();
        box2 = Box.createHorizontalBox();
        boxfirst = Box.createHorizontalBox();

        boxfirst.add(label1);

        box1.add(Box.createVerticalStrut(8));
        box1.add(scrollPane);  // 使用包装后的JScrollPane
        
        box1.add(Box.createVerticalStrut(8));
        box2.add(submit);
        box2.add(Box.createHorizontalStrut(100));
        box2.add(remake);
        basebox.add(boxfirst);
        basebox.add(box1);
        basebox.add(box2);
        add(basebox);

        //监视器
        submit.addActionListener(controller);
        controller.setguessMVC(this);
        validate();

        remake.addActionListener(controller2);
        controller2.setguessMVC(this);
        validate();
    }
}





// public class guessMVC extends JFrame {

//     guess guess = new guess();

//     JButton submit;
//     JLabel label1;
//     JTextArea text;
//     Box basebox,box1,box2;

//     guessController controller;

//     guessMVC(){
//         setLayout(new java.awt.FlowLayout());
//         init();
//         setVisible(true);
//         setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//     }

//     void init(){

//         label1 = new JLabel("请在方框中输入多卷坯布的长度");
//         submit = new JButton("提交");
//         text = new JTextArea(10, 8);

//         basebox =Box.createVerticalBox();
//         box1 = Box.createVerticalBox();
//         box2 = Box.createVerticalBox();
//         box1.add(Box.createVerticalStrut(8));
//         box1.add(text);
//         box1.add(Box.createVerticalStrut(8));
//         box2.add(submit);
//         basebox.add(label1);
//         basebox.add(box1);
//         basebox.add(box2);
//         add(basebox);
        
//         controller = new guessController();
//         submit.addActionListener(controller);
//         controller.setguessMVC(this);
//         validate();
//     }
// }
