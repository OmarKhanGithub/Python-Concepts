package a_java_package;
import java.util.Scanner;


public class TicTacToe {
    public static void main(String[] args) {

        String value;
        int counter = 0;
        String response;

        String[] firstRow = new String[]{" ", " ", " "};
        String[] secondRow = new String[]{" ", " ", " "};
        String[] thirdRow = new String[]{" ", " ", " "};

        System.out.println("Time to play Tic-tac-toe!\n");

        boolean gameOver = false;
        while(!gameOver){

            int playerNum = playersTurn(counter);

            if(playerNum == 1){
                System.out.println("Player 1:");
                System.out.println("----------:");
                value = "X";
                response = choice(value, firstRow, secondRow, thirdRow);
                if (response.equals("Error")){
                    counter++;
                }

            } else if ((playerNum == 2)){
                System.out.println("Player 2:");
                System.out.println("----------:");

                value = "O";
                response = choice(value, firstRow, secondRow, thirdRow);
                if (response.equals("Error")){
                    counter++;
                }
            }

            System.out.println("\n " + firstRow[0] + " | " + firstRow[1] + " | " + firstRow[2] + " ");
            System.out.println("-----------");
            System.out.println(" " + secondRow[0] + " | " + secondRow[1] + " | " + secondRow[2] + " ");
            System.out.println("-----------");
            System.out.println(" " + thirdRow[0] + " | " + thirdRow[1] + " | " + thirdRow[2] + " " + "\n");

            counter++;
            gameOver = hasGameBeenWon(firstRow, secondRow, thirdRow);
        }
    }

    private static int playersTurn(int counter){
        int playerNumber;

        if (counter % 2 == 0){
            playerNumber = 1;
        } else {
            playerNumber = 2;
        }
        return playerNumber;
    }

    private static String choice(String value, String[] firstRow, String[] secondRow,  String[] thirdRow){
        Scanner row = new Scanner(System.in);
        System.out.print("Enter the row of your mark: ");
        int rowChoice = row.nextInt();

        Scanner column = new Scanner(System.in);
        System.out.print("Enter the column of your mark:");
        int columnChoice = column.nextInt();

        if (rowChoice == 1){
            if (columnChoice == 1) return firstRow[0] = value;
            else if (columnChoice == 2) return firstRow[1] = value;
            else if (columnChoice == 3) return firstRow[2] = value;


        } else if (rowChoice == 2) {
            if (columnChoice == 1) return secondRow[0] = value;
            else if (columnChoice == 2) return secondRow[1] = value;
            else if (columnChoice == 3) return secondRow[2] = value;

        } else if (rowChoice == 3) {
            if (columnChoice == 1) return thirdRow[0] = value;
            else if (columnChoice == 2) return thirdRow[1] = value;
            else if (columnChoice == 3) return thirdRow[2] = value;

        }
        System.out.println("----------------------");
        System.out.println("NOT A REASONABLE INPUT, BUDDY! \nTRY AGAIN!");
        return "Error";

    }

    private static boolean hasGameBeenWon(String[] firstRow, String[] secondRow, String[] thirdRow){
        boolean gameOver;

        if((firstRow[0].equals("X") && firstRow[1].equals("X") && firstRow[2].equals("X")) ||
                (secondRow[0].equals("X") && secondRow[1].equals("X") && secondRow[2].equals("X")) ||
                (thirdRow[0].equals("X") && thirdRow[1].equals("X") && thirdRow[2].equals("X")) ||
                (firstRow[0].equals("X") && secondRow[0].equals("X") && thirdRow[0].equals("X")) ||
                (firstRow[1].equals("X") && secondRow[1].equals("X") && thirdRow[1].equals("X")) ||
                (firstRow[2].equals("X") && secondRow[2].equals("X") && thirdRow[2].equals("X")) ||
                (firstRow[0].equals("X") && secondRow[1].equals("X") && thirdRow[2].equals("X")) ||
                (firstRow[2].equals("X") && secondRow[1].equals("X") && thirdRow[0].equals("X"))
                ) {
            System.out.println("PLAYER 1 WINS!");
            gameOver = true;

        } else if ((firstRow[0].equals("O") && firstRow[1].equals("O") && firstRow[2].equals("O")) ||
                    (secondRow[0].equals("O") && secondRow[1].equals("O") && secondRow[2].equals("O")) ||
                    (thirdRow[0].equals("O") && thirdRow[1].equals("O") && thirdRow[2].equals("O")) ||
                    (firstRow[0].equals("O") && secondRow[0].equals("O") && thirdRow[0].equals("O")) ||
                    (firstRow[1].equals("O") && secondRow[1].equals("O") && thirdRow[1].equals("O")) ||
                    (firstRow[2].equals("O") && secondRow[2].equals("O") && thirdRow[2].equals("O")) ||
                    (firstRow[0].equals("O") && secondRow[1].equals("O") && thirdRow[2].equals("O")) ||
                    (firstRow[2].equals("O") && secondRow[1].equals("O") && thirdRow[0].equals("O"))
                    ) {
            System.out.println("PLAYER 2 WINS!");
            gameOver = true;

        } else {
            gameOver = false;

        }
        return gameOver;

    }

}
