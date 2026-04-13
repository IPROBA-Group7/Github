import java.sql.*;
import java.util.*;

public class BadExample {

    private static final String API_KEY = "12345-SECRET-KEY-ABCDE";

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter username:");
        String username = sc.nextLine();

        String query = "SELECT * FROM users WHERE username = '" + username + "'";

        try {
            Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "root");
            Statement stmt = conn.createStatement();

            ResultSet rs = stmt.executeQuery(query);

            while (rs.next()) {
                System.out.println("User: " + rs.getString("username"));
            }

        } catch (Exception e) {
            System.out.println("Something went wrong");
        }

    }

    public static void doStuff() {
        int x = 0;
        for (int i = 0; i < 1000; i++) {
            x += i;
        }
        System.out.println(x);
    }
}
