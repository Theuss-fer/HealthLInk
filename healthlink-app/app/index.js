import { useEffect,useRef } from "react";
import {Animated, StyleSheet} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import {useRouter} from 'expo-router';



export default function Splash(){
    const router = useRouter();

    const scale = useRef(new Animated.Value(0.5)).current;
    const opacity = useRef(new Animated.Value(0)).current;

    useEffect(()=> {
        Animated.parallel([
            Animated.timing(scale, {
                toValue: 1,
                duration: 1000,
                useNativeDriver: true,
            }),
            Animated.timing(opacity,{ 
                duration: 1200,
                toValue: 1,
                useNativeDriver: true,
            })
        ]). start();

        const timer = setTimeout(() => {
            router.replace('/login')
        }, 3200)

        return () => clearTimeout(timer);
    }, []);

    return(
        <LinearGradient
        colors={["#1E88E5", "#43A047", "#fff"]}
        style={styles.container}
        >
            <Animated.Image
                source={require("../assets/IMG/HealthLink-logo.png")}
                style={[styles.logo, {transform: [{ scale}], opacity}, ]}
                resizeMode="contain "
            />
        </LinearGradient>
    )
}

const styles = StyleSheet.create({
    
  container: {
    flex: 1,    
    justifyContent: "center",
    alignItems: "center",
  },
  logo: {
    width: 300,
    height: 300,
    
  },
});