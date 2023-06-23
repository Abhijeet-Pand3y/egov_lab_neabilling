 internal class AreaSum
    {
        public double addArea(List<object> shapes)
        {
            double sum = 0;

            foreach (object shape in shapes)
            {
                if(shape is Circle)
                {

                    int r = ((Circle)shape).getRadius();
                    sum += Math.PI * r * r;
                }
                else if(shape is Square)
                {
                    int l = ((Square)shape).getLength();
                    sum += l * l;
                }
            }
            
            return sum;
        }
    }