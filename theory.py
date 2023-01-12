
import streamlit as st

FFP = '''Froth flotation is an important concentration process that can be used to selectively separate hydrophobic materials from hydrophilic waste gangue. In a more simple context, froth flotation is one of the most popular operational processes for mineral beneficiation. In ore/mineral beneficiation, froth flotation is a method by which commercially important minerals are separated from impurities and other minerals by collecting them on the surface of a froth layer.

Flotation is the process of separation of beneficial minerals from a mixture by creating froth on which minerals separate out. This method of froth floatation is a method of mineral processing in which different minerals are separated selectively. Such ores containing multiple metals such as lead, copper and zinc can be selectively extracted by using froth floatation. The minerals that do not float into the froth are called the flotation tailings or flotation tails.

The froth flotation process was first patented by H. F. K. Pickard, E. L.Sulman and John Ballot in the year 1906. This was nearly 19 years after the first cyanide process patents that were filed by MacArthur and the Forests. This process came into light while the scientists were experimenting with the Cattermole process.'''

MFF = '''The method of froth floatation can be classified into three steps:

1. True floatation – In this process minerals are selectively attached to froth. This process is very critical and important as the extraction of the valuable minerals is decided by this step only while the other two steps determine the separation efficiency between the mineral and the gangue.

2. Entrainment – Under this process of entrainment air bubbles are passed in liquid water to which the froth leads to the generation of air bubbles.

3. Aggregation – In this process, the mineral particles are trapped by the froth.

An important criterion of the separation of minerals by the froth floatation method is that the size of the particles of the ores must be very small equivalent to powder form. This is very important because the heavier and bigger particle would require a greater adhesive force without which they would no longer attach to the froth and settle down in the bottom. Thus separation will not be possible.

Froth flotation is mainly operated under two common techniques :

1. Direct floatation technique – In this method, the mineral sticks to the air bubble and the remaining gangue settles down at the bottom.

2. Reverse floatation technique – In this method, the gangue sticks to the air bubble and ore particles settle down in the bottom.'''

BPOFFP1 = '''The process of froth floatation starts with the Comminution process in which the surface area of the ore is increased. First of all, the ores are crushed into very fine powder-sized particles and mixed with water. The mixture obtained is called Slurry. A Collector which acts as a surfactant chemical is added to the slurry. This is done to enhance the hydrophobic nature of the mineral.

The slurry has now been converted into pulp. This pulp is added to the container filled with water and then air jets are forced into it to create bubbles. The required mineral is repelled by water and thus gets attached to the air bubbles. As these air bubbles rise up to the surface with mineral particles sticking to them, these are called froth. This Froth is separated and further taken for the next process of refining and extraction.'''



BPOFFP2 = '''When we dealing with the process of froth flotation
we should note that it is not solely dependent upon the
density of the material. In addition, the froth flotation process
is also dependent upon its hydrophobic nature. For example, as we
have discussed above froth flotation is a technique that is used
widely in the mining industry. Using this technique, particles of
interest are physically separated from a liquid phase. This can be
done mainly due to the differences in the ability of air bubbles to
selectively adhere to the surface of the particles which is again based
on their hydrophobicity. The hydrophobic particles containing the air
bubbles that are attached to it are carried to the surface. This results
in the formation of the froth that can be removed. Hydrophilic materials
usually remain in the liquid phase.'''


MOFFP = '''The basic principle applied in the process of Froth Flotation is the difference in the wetting ability of the ore and remaining impurities. The particles are categorized into two types on the basis of their wetting ability;

1. Hydrophobic
2. Hydrophilic
If the minerals are of Hydrophobic nature then only can get attracted toward froth and not with water. Once these minerals come to the surface with the help of buoyant force applied on the froth, the particle-bubble contact will be intact only when there is the formation of a stabilized foam. The deciding factor of the stability of the froth is the strength of the attachment of the bubble to the mineral. This is calculated with the help of YOUNG-DUPRE EQUATION. This equation gives the relation between the strength of attachment and the interfacial energies.'''

FE = '''Flotation is typically conducted in rectangular or cylindrical mechanically agitated cells or tanks including flotation columns, Jameson Cells or deinking flotation machines. While this method is based on the air absorption concept, there are significantly two distinct groups of flotation equipment namely pneumatic and mechanical machines. With pneumatic machines, we obtain low-grade concentrate and little operating trouble.

Mechanical cells, on the other hand, have a large mixer and diffuser mechanism at the bottom of the mixing tank. This is set in such a way as to allow air to flow and provide seamless mixing action. Flotation columns also make use of air spargers that allows us to introduce air at the bottom of a tall column. The slurry is introduced above. The motion of the slurry flowing downwards and the air flowing upwards sort of generates a mixing action. Mechanical cells have a high throughput rate. However, the material produced is of lower quality.'''

FFC = '''The setup in which the froth floatation process is carried out is called the froth floatation column.

A common industrial column cell consists of a long cylindrical tank fitted with a feed inlet pipe in the upper portion of the cylinder. Two launders are also connected, one internally and one externally to collect and separate the foam. In the lower portion of the cylinder, an outlet pipe is also connected to remove the slurry and the non -floating material. Pipes for proper drainage and many nozzles for re-pulping are also fitted in the lower section of the column.
'''


LOCU = '''In order to maintain uniform quality of froth and optimize the adhesive quality of the minerals, different chemicals are required to be mixed in the slurry. Some of such important chemicals are listed below.

1. Collector
2. Frother
3. Regulator
4. Activator
5. Depressant
6. pH Modifier'''

AD = '''Some of the advantages of froth flotation are:

Almost all types of minerals can be separated by this process.
Surface properties can be controlled and altered by the flotation reagent.
This technique is highly appropriate for the separation of sulphide minerals.
The main disadvantage of the froth flotation process is that this method is highly complex and expensive. The results can vary as it can be easily influenced by the slime.'''

def Theory():
    st.header('What is Froth Flotation Process ?')
    st.write(FFP)
    st.header('Method of Froth Floatation')
    st.write(MFF)
    st.header('Basic Principle of Froth Flotation Process')
    st.write(BPOFFP1)
    st.image('flotation1.png')
    st.write(BPOFFP2)
    st.header('Mechanism of Froth Flotation Process')
    st.write(MOFFP)
    st.header('Floatation Equipment')
    st.write(FE)
    st.header('Froth Floatation Column')
    st.write(FFC)
    st.image('flotation3.png')
    st.header('List Of Chemicals Used')
    st.write(LOCU)
    st.header('Advantages and Disadvantages of Froth Flotation')
    st.write(AD)

























