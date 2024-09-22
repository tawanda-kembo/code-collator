import React, { useState, useEffect } from 'react';
import { StyleSheet, TextInput, Switch, Button, Alert } from 'react-native';
import { doc, setDoc, getDoc } from 'firebase/firestore';
import { signOut } from 'firebase/auth';
import { auth, db } from '../../firebaseConfig';
import { useRouter } from 'expo-router';

import { Text, View } from '@/components/Themed';

export default function ProfileScreen() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [emailNotifications, setEmailNotifications] = useState(false);
  const [smsNotifications, setSmsNotifications] = useState(false);
  const router = useRouter();

  useEffect(() => {
    loadProfile();
  }, []);

  const loadProfile = async () => {
    if (auth.currentUser) {
      const docRef = doc(db, 'users', auth.currentUser.uid);
      const docSnap = await getDoc(docRef);

      if (docSnap.exists()) {
        const data = docSnap.data();
        setName(data.name || '');
        setEmail(data.email || '');
        setPhone(data.phone || '');
        setEmailNotifications(data.emailNotifications || false);
        setSmsNotifications(data.smsNotifications || false);
      }
    }
  };

  const handleSave = async () => {
    if (auth.currentUser) {
      try {
        await setDoc(doc(db, 'users', auth.currentUser.uid), {
          name,
          email,
          phone,
          emailNotifications,
          smsNotifications,
        });
        Alert.alert('Success', 'Profile saved successfully!');
      } catch (error) {
        Alert.alert('Error', 'Failed to save profile. Please try again.');
      }
    }
  };

  const handleLogout = async () => {
    try {
      await signOut(auth);
      router.replace('/auth');
    } catch (error) {
      Alert.alert('Error', 'Failed to log out. Please try again.');
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Your Profile</Text>
      <TextInput
        style={styles.input}
        placeholder="Name"
        value={name}
        onChangeText={setName}
      />
      <TextInput
        style={styles.input}
        placeholder="Email"
        value={email}
        onChangeText={setEmail}
        keyboardType="email-address"
      />
      <TextInput
        style={styles.input}
        placeholder="Phone"
        value={phone}
        onChangeText={setPhone}
        keyboardType="phone-pad"
      />
      <View style={styles.switchContainer}>
        <Text>Email Notifications</Text>
        <Switch
          value={emailNotifications}
          onValueChange={setEmailNotifications}
        />
      </View>
      <View style={styles.switchContainer}>
        <Text>SMS Notifications</Text>
        <Switch
          value={smsNotifications}
          onValueChange={setSmsNotifications}
        />
      </View>
      <Button title="Save Profile" onPress={handleSave} />
      <View style={styles.logoutButtonContainer}>
        <Button title="Log Out" onPress={handleLogout} color="red" />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 10,
    paddingHorizontal: 10,
  },
  switchContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 10,
  },
  logoutButtonContainer: {
    marginTop: 20,
  },
});