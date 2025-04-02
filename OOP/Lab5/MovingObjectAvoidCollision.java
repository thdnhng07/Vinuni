// VinUniversity, Spring 2025
// COMP1020 Object-Oriented Programming and Data Structures
// Lab 05 – Week 05
// by Dat Thanh – V202401381
// Date: Mar 21, 2025
// Disclaimer: I certify that this assignment is my own work and that I have not copied in part
// or whole or otherwise plagiarised the work of other students and/or persons.
//----------------------------------Problem 2-------------------------------
//                        Moving Object Avoid Collision
//-----------------------------------------------------------------------------
package Lab5;

import java.io.BufferedReader ;
import java.io .FileReader ;
import java.io.InputStreamReader ;
import java.io.PrintWriter ;
import java.util.*;

// Interface for movement and collision handling
interface MoveObject {
    void move();
    void moveOpposite();
    boolean collideIfMove(MoveObject o);
    boolean collide(MoveObject o);
    String getID();
}

// Base class for all objects
class BaseObject {
    public String ID;
    public String direction;
    public int speed;

    public BaseObject(String ID, String direction, int speed) {
        this.ID = ID;
        this.direction = direction;
        this.speed = speed;
    }

    public void changeDirection(String direction, int speed) {
        this.direction = direction;
        this.speed = speed;
    }
}

// Rectangle Object
class MRectangle extends BaseObject implements MoveObject {
    public int x, y;
    public int LX, LY;

    public MRectangle(String ID, String direction, int speed, int x, int y, int LX, int LY) {
        super(ID, direction, speed);
        this.x = x;
        this.y = y;
        this.LX = LX;
        this.LY = LY;
    }

    // TODO
    @Override
    public void move() {
        switch (direction) {
            case "L": x -= speed; break;
            case "R": x += speed; break;
            case "U": y += speed; break;
            case "D": y -= speed; break;
        }
    }

    // TODO
    @Override
    public void moveOpposite() {
        switch (direction) {
            case "L": x += speed; break;
            case "R": x -= speed; break;
            case "U": y -= speed; break;
            case "D": y += speed; break;
        }
    }

    // TODO
    @Override
    public boolean collideIfMove(MoveObject o) {
        move();
        boolean isColliding = collide(o);
        moveOpposite();
        return isColliding;
    }

    // TODO
    @Override
    public boolean collide(MoveObject o) {
        if (o instanceof MCircle) {
            MCircle c = (MCircle) o;
            int closestX = Math.max(x - LX, Math.min(c.x, x + LX));
            int closestY = Math.max(y - LY, Math.min(c.y, y + LY));
            int distanceSq = (closestX - c.x) * (closestX - c.x) + (closestY - c.y) * (closestY - c.y);
            return distanceSq <= c.radius * c.radius;
        } else if (o instanceof MRectangle) {
            MRectangle r = (MRectangle) o;
            return Math.abs(x - r.x) <= (LX + r.LX) && Math.abs(y - r.y) <= (LY + r.LY);
        }
        return false;
    }

    @Override
    public String getID() {
        return ID;
    }

    @Override
    public String toString() {
        return x + " " + y;
    }
}

// Circle Object
class MCircle extends BaseObject implements MoveObject {
    public int x, y;
    public int radius;

    public MCircle(String ID, String direction, int speed, int x, int y, int radius) {
        super(ID, direction, speed);
        this.x = x;
        this.y = y;
        this.radius = radius;
    }

    // TODO
    @Override
    public void move() {
        switch (direction) {
            case "L": x -= speed; break;
            case "R": x += speed; break;
            case "U": y += speed; break;
            case "D": y -= speed; break;
        }
    }

    // TODO
    @Override
    public void moveOpposite() {
        switch (direction) {
            case "L": x += speed; break;
            case "R": x -= speed; break;
            case "U": y -= speed; break;
            case "D": y += speed; break;
        }
    }

    // TODO
    @Override
    public boolean collideIfMove(MoveObject o) {
        move();
        boolean isColliding = collide(o);
        moveOpposite();
        return isColliding;
    }

    // TODO
    @Override
    public boolean collide(MoveObject o) {
        if (o instanceof MCircle) {
            MCircle c = (MCircle) o;
            int dx = this.x - c.x;
            int dy = this.y - c.y;
            int distanceSq = dx * dx + dy * dy;
            return distanceSq <= (this.radius + c.radius) * (this.radius + c.radius);
        } else if (o instanceof MRectangle) {
            return o.collide(this);
        }
        return false;
    }

    @Override
    public String getID() {
        return ID;
    }

    @Override
    public String toString() {
        return x + " " + y;
    }
}

// Main class for object simulation
public class MovingObjectAvoidCollision {
    ArrayList<MoveObject> objects = new ArrayList<>();

    MoveObject findByID(String ID) {
        for (MoveObject o : objects)
            if (o.getID().equals(ID)) return o;
        return null;
    }

    public void run() {
        try {
            BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
            String line;
            String[] s;

            while (true) {
                line = in.readLine();
                if (line.equals("#")) break;

                s = line.split(" ");

                if (s[0].equals("create")) {
                    String TYPE = s[1];
                    String ID = s[2];

                    if (TYPE.equals("RECTANGLE")) {
                        int x = Integer.parseInt(s[3]);
                        int y = Integer.parseInt(s[4]);
                        int LX = Integer.parseInt(s[5]);
                        int LY = Integer.parseInt(s[6]);
                        String direction = s[7];
                        int speed = Integer.parseInt(s[8]);

                        MRectangle r = new MRectangle(ID, direction, speed, x, y, LX, LY);
                        boolean ok = true;
                        for (MoveObject o : objects) {
                            if (r.collide(o)) { ok = false; break; }
                        }
                        if (ok) objects.add(r);
                    } else if (TYPE.equals("CIRCLE")) {
                        int x = Integer.parseInt(s[3]);
                        int y = Integer.parseInt(s[4]);
                        int radius = Integer.parseInt(s[5]);
                        String direction = s[6];
                        int speed = Integer.parseInt(s[7]);

                        MCircle c = new MCircle(ID, direction, speed, x, y, radius);
                        boolean ok = true;
                        for (MoveObject o : objects) {
                            if (c.collide(o)) { ok = false; break; }
                        }
                        if (ok) objects.add(c);
                    }
                } else if (s[0].equals("move")) {
                    String ID = s[1];
                    MoveObject o = findByID(ID);
                    if (o != null) {
                        boolean okMove = true;
                        for (MoveObject oo : objects)
                            if (oo != o && o.collideIfMove(oo)) {
                                okMove = false;
                                break;
                            }
                        if (okMove) o.move();
                    }
                } else if (s[0].equals("change_direction")) {
                    String ID = s[1];
                    String direction = s[2];
                    int speed = Integer.parseInt(s[3]);
                    MoveObject o = findByID(ID);
                    if (o instanceof BaseObject) ((BaseObject) o).changeDirection(direction, speed);
                } else if (s[0].equals("view_position")) {
                    String ID = s[1];
                    MoveObject o = findByID(ID);
                    System.out.println(o == null ? "NULL" : o);
                }
            }
        } catch (Exception e) { e.printStackTrace(); }
    }

    public static void main(String[] args) {
        MovingObjectAvoidCollision app = new MovingObjectAvoidCollision();
        app.run();
    }
}