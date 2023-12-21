package 坯布计数器;

public class guess {
    public double sum;
    public double[] order = new double[100];

    public String toString() {
        StringBuilder progress = new StringBuilder();
        for (int i = 1; i < order.length; i++) {
            if (order[i] == 0&&i!=0) {
                break;
            }
            if(i%4==0&&i!=0){
                progress.append(order[i]).append("\n");
            }else{
                progress.append(order[i]).append("  ::  ");
            }
            
        }
        String answer = progress + "\n\n总计长度为:" + sum;
        return answer;
    }
}

