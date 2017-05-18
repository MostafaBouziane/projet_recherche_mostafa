
#------------------------------------ Dirichlet process et echantillonnage de Gibbs-------------------------------------------
Dirichlet<- function(observations,iterations,alpha) {
    nbrp <- c(length(observations[,1]))  
    print(nbrp);     
    ParamOfClusters <- list()
    saving <- rep(1,iterations)
    clusters <- rep(1,nrow(observations))
    for (i in 1:max(clusters)) ParamOfClusters [[i]] <-Param_Update(observations[clusters==i,])   
        for (m  in 1:iterations) {
        for (i in 1:nrow(observations) ){
             
            nbrp [clusters[i]] <- nbrp [clusters[i]] - 1
            if (nbrp [clusters[i]]!=0) {

            ParamOfClusters [[clusters[i]]] <- Param_Update(observations[clusters == clusters[i],]) 

     } else { 
                ParamOfClusters [[ clusters[i] ]] <- NULL
                nbrp <- nbrp [-clusters[i]]
                clusters[ clusters>clusters[i] ] <-  clusters[ clusters>clusters[i] ] - 1 
                   }
            
            process <- log(c(nbrp,alpha)) 
            for (k in 1:length(ParamOfClusters)){
                process[k] <- process[k] + LogofLik(ParamOfClusters[[k]],observations[i,]);
                }
            process <- exp(process - max(process)); 
            process <- process / sum(process);
                 
            
            clusters[i] <- Tirage_multinomial(process)
            if (length(nbrp ) < clusters[i]) nbrp [clusters[i]]<-0 
            nbrp [clusters[i]] <- nbrp [clusters[i]] + 1
            ParamOfClusters [[clusters[i]]] <- Param_Update(observations[clusters == clusters[i],])
        }

saving[m] <- max(clusters)
}
print(saving);
print(table(factor(saving)));
plot(observations,col=clusters)
return(clusters);
        
}

#--------------------------------------Fonctions utilisées à l'intérieur de l'algorithme---------------------------------------------------
Tirage_multinomial <- function (x) {
    a <- runif(1)
    b <- 0
    for (i in 1:length(x)) {
        b <- b + x[i]
        if (a<b) break;
        }
    return(i) 
    }

Param_Update <- function (datas) {
    if (is.vector(datas)) datas<-matrix(datas,nrow=1)
    p <- c()
    for (i in 1:ncol(datas) ) {
        m <- mean( datas[,i] )
        s <-   sd( datas[,i] )
        if (is.na(s)) s<-1  
        p <- c(p,m,s) 
    }
    return(p)
}
    
    LogofLik <- function(params,data) {
    lg <- 0;
    for (i in 1:length(data) ) {
        m <- params[2*(i)-1]
        s <- params[2*(i)]
        lg <- lg + dnorm(data[i], m, s, log=TRUE)
    }
    return(lg)  
}
