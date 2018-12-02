#include <iostream>
#include <array>
#include <cstdlib>
#include <fstream>
#include <cmath>
#include <time.h>

// useful constants
const float G = 1;
const float dt = 0.0001;
const float tmax = 10;
const float t0 = 0;
const int nObj = 2000;

const bool relat = false;
const bool loop = false;


//nObj  150



float computeDistance(double x1, double y1, double x2, double y2)
{
    float d = pow((y2-y1)*(y2-y1) + (x2-x1)*(x2-x1), 0.5);
    return(d);
}



void updateCoord(std::array<float, nObj> &rMin, std::array<float, nObj> &allM, 
                std::array<bool, nObj> &status, std::array<double, nObj> &allX, 
                std::array<double, nObj> &allY, std::array<float, nObj> &allVx,
                std::array<float, nObj> &allVy)
{
    //for (int i = 0; i<nObj+2; i++){
    //    std::cout << rMin[i] << std::endl;
    //}
    for (int i = 0; i<nObj; i++){
        rMin[i] = pow(allM[i],0.3)/15;     
    }

    for (int i = 0; i < nObj; i++){
        for (int j = 0; j < nObj; j++)
        {
            if (j < i && status[i] == 1 && status[j] == 1)
            {
                float r = computeDistance(allX[i], allY[i], allX[j], allY[j]);
                float rmin = std::max(rMin[i], rMin[j]);

                if (r < rmin)
                {
                    float Mi = allM[i];
                    float Mj = allM[j];
                    std::cout << "==============================" << std::endl;
                    std::cout << "boom!, " << i << ' ' << j << std::endl;
                    //std::cout << allX[i] << ' ' << allY[i] << std::endl;
                    //std::cout << allX[j] << ' ' << allY[j] << std::endl;

                    allVx[i] = (Mi*allVx[i] + Mj*allVx[j])/(Mi + Mj);
                    allVy[i] = (Mi*allVy[i] + Mj*allVy[j])/(Mi + Mj);
                    allX[i] = (Mi*allX[i] + Mj*allX[j])/(Mi + Mj);
                    allY[i] = (Mi*allY[i] + Mj*allY[j])/(Mi + Mj);
                    allM[i] += allM[j];

                    status[j] = false;
               
                }
                if(relat==false)
                {
                    float F = G * allM[i] * allM[j] / (r*r);
                    float Fx = F * (allX[j]-allX[i]) / r;
                    float Fy = F * (allY[j]-allY[i]) / r;

                    allVx[i] += Fx / allM[i] * dt;
                    allVy[i] += Fy / allM[i] * dt;
                    allVx[j] += -Fx / allM[j] * dt;
                    allVy[j] += -Fy / allM[j] * dt;

                    allX[i] = (allX[i] + allVx[i] * dt);
                    allY[i] = (allY[i] + allVy[i] * dt);
                    allX[j] = (allX[j] + allVx[j] * dt);
                    allY[j] = (allY[j] + allVy[j] * dt);
                }

                else if (relat==true)
                {
                    //se estidua la órbita de j
                
                    float alpha = atan((allY[j]-allY[i])/(allX[j]-allX[i]));
                    float beta = atan(allVy[j]/allVx[j]);

                    float L = allM[j] * r * pow(allVx[j]*allVx[j] + allVy[j]*allVy[j], 0.5) * sin(beta-alpha);
                    //float L = 1;
                    //if (L>10e3)
                    //std::cout << "v vale " << allVx[j] <<' '<< r << std::endl;
                    
                    float F = +3*G*L*L*allM[i]/(allM[j]*pow(r, 4)) + G*allM[j]*allM[i]/(r*r) - L*L/pow(r, 3);
                    float Fx = F * (allX[j]-allX[i]) / r;
                    float Fy = F * (allY[j]-allY[i]) / r;
                    allVx[i] += Fx / allM[i] * dt;
                    allVy[i] += Fy / allM[i] * dt;
                    allVx[j] += -Fx / allM[j] * dt;
                    allVy[j] += -Fy / allM[j] * dt;

                    allX[i] = (allX[i] + allVx[i] * dt);
                    allY[i] = (allY[i] + allVy[i] * dt);
                    allX[j] = (allX[j] + allVx[j] * dt);
                    allY[j] = (allY[j] + allVy[j] * dt);

                }
                if (loop==true)
                {   
                    int lim=10;
                    if (allX[i] > lim){allX[i] -= 2*lim;}
                    else if (allX[i] < -lim){allX[i] += 2*lim;}
                    if (allY[i] > lim){allY[i] -= 2*lim;}
                    else if (allY[i] < -lim){allY[i] += 2*lim;}
                    if (allX[j] > lim){allX[j] -= 2*lim;}
                    else if (allX[j] < -lim){allX[j] += 2*lim;}
                    if (allY[j] > lim){allY[j] -= 2*lim;}
                    else if (allY[j] < -lim){allY[j] += 2*lim;}
                }
            }
        }
    }
} 






int main()
{
    clock_t tStart = clock();
    int num_timesteps = (tmax-t0)/dt;

    //inicialize main arrays
    std::array<double, nObj> allX;
    std::array<double, nObj> allY;

    std::array<float, nObj> allVx;
    std::array<float, nObj> allVy;

    std::array<float, nObj> allM;
    std::array<bool, nObj> status;

    //fill with initial random values
    for (int i = 0; i < nObj; i++){
        allX[i] = (double) rand()/RAND_MAX * 20 - 10;
        allY[i] = (double) rand()/RAND_MAX * 20 - 10;

        allVx[i] = (double) rand()/RAND_MAX - 0.5;
        allVy[i] = (double) rand()/RAND_MAX - 0.5;

        //orbital conditions
        float scale=10;

        //allVx[i] = (double) -allY[i]/scale;
        //allVy[i] = (double) allX[i]/scale;

        //allM[i] = (double) rand()/RAND_MAX * 20;
        allM[i] = 3;
        
        status[i] = true;
    }

    //allX[0] = 0;
    //allY[0] = 0;
    //allVx[0] = 0;
    //allVy[0] = 0;
    //allM[0] = 200;



    // main loop
    std::ofstream file;
    file.open("temp.txt");
    //c -> central particle
    //l -> boundary restrictions
    

    std::array<double, nObj> xFinalTemp;
    std::array<double, nObj> yFinalTemp;

    std::array<float, nObj> rMin;
    float t = t0;
    while (t <= tmax)
    {
        //std::cout << "good1" << std::endl;

        updateCoord(rMin, allM, status, allX, allY, allVx, allVy);
        
        file << t << ' ';
        bool somethingRemains = false;
        for (int i = 0; i < nObj; i++)
        {
            if (allX[i] != xFinalTemp[i] && allY[i] != yFinalTemp[i])
            {
                somethingRemains = true;
                //std::cout << xFinalTemp[i] << ' ' << allX[i] << std::endl;
                xFinalTemp[i] = allX[i];
                yFinalTemp[i] = allY[i];

                file << allM[i] << ' ' << allX[i] << ' ' << allY[i] << ' ';
            }
            
        }
        if (somethingRemains == false) break;
        file << '\n';


        t += dt;
    }
    printf("Time taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);

    file.close();
}