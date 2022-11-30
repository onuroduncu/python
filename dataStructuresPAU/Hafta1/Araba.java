public class Araba implements Comparable<Araba>{
    public int modelYili;
    public String plaka;
    public String marka;
    public double motorHacmi;
public Araba(String marka,int modelYili,double motorHacmi, String plaka){
    this.marka=marka;
    this.modelYili=modelYili;
    this.motorHacmi=motorHacmi;
    this.plaka=plaka;
}
@Override
public int compareTo(Araba o){
    if(o.modelYili<this.modelYili) return 1;
    if(o.modelYili>this.modelYili) return -1;
	else return 0;
}
}