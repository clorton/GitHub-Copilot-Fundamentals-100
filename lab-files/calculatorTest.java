import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class CalculatorTest {
    
    @Test
    public void testAdd() {
        double result = Calculator.add(5.0, 3.0);
        assertEquals(8.0, result);
    }
    
    @Test
    public void testSubtract() {
        double result = Calculator.subtract(5.0, 3.0);
        assertEquals(2.0, result);
    }
    
    @Test
    public void testMultiply() {
        double result = Calculator.multiply(5.0, 3.0);
        assertEquals(15.0, result);
    }
    
    @Test
    public void testDivide() {
        double result = Calculator.divide(6.0, 3.0);
        assertEquals(2.0, result);
    }
}