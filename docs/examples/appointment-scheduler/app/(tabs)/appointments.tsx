import React, { useState, useEffect } from 'react';
import { StyleSheet, ScrollView, Button, Alert, FlatList } from 'react-native';
import { Calendar } from 'react-native-calendars';
import { collection, addDoc, query, where, getDocs, deleteDoc, doc } from 'firebase/firestore';
import { auth, db } from '../../firebaseConfig';

import { Text, View } from '@/components/Themed';

const TIME_SLOTS = [
  '09:00', '10:00', '11:00', '12:00', '14:00', '15:00', '16:00', '17:00'
];

export default function AppointmentsScreen() {
  const [selected, setSelected] = useState('');
  const [availableSlots, setAvailableSlots] = useState(TIME_SLOTS);
  const [userAppointments, setUserAppointments] = useState([]);

  useEffect(() => {
    if (selected) {
      fetchBookedSlots();
    }
    fetchUserAppointments();
  }, [selected]);

  const fetchBookedSlots = async () => {
    const appointmentsRef = collection(db, 'appointments');
    const q = query(appointmentsRef, where('date', '==', selected));
    const querySnapshot = await getDocs(q);
    const bookedSlots = querySnapshot.docs.map(doc => doc.data().time);
    setAvailableSlots(TIME_SLOTS.filter(slot => !bookedSlots.includes(slot)));
  };

  const fetchUserAppointments = async () => {
    if (auth.currentUser) {
      const appointmentsRef = collection(db, 'appointments');
      const q = query(appointmentsRef, where('userId', '==', auth.currentUser.uid));
      const querySnapshot = await getDocs(q);
      const appointments = querySnapshot.docs.map(doc => ({
        id: doc.id,
        ...doc.data()
      }));
      setUserAppointments(appointments);
    }
  };

  const bookAppointment = async (time: string) => {
    try {
      await addDoc(collection(db, 'appointments'), {
        userId: auth.currentUser?.uid,
        date: selected,
        time: time,
      });
      Alert.alert('Success', 'Appointment booked successfully!');
      fetchBookedSlots();
      fetchUserAppointments();
    } catch (error) {
      Alert.alert('Error', 'Failed to book appointment. Please try again.');
    }
  };

  const cancelAppointment = async (appointmentId: string) => {
    try {
      await deleteDoc(doc(db, 'appointments', appointmentId));
      Alert.alert('Success', 'Appointment cancelled successfully!');
      fetchUserAppointments();
    } catch (error) {
      Alert.alert('Error', 'Failed to cancel appointment. Please try again.');
    }
  };

  const renderAppointment = ({ item }) => (
    <View style={styles.appointmentItem}>
      <Text>{`Date: ${item.date}, Time: ${item.time}`}</Text>
      <Button title="Cancel" onPress={() => cancelAppointment(item.id)} color="red" />
    </View>
  );

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Book an Appointment</Text>
      <Calendar
        onDayPress={day => {
          setSelected(day.dateString);
        }}
        markedDates={{
          [selected]: { selected: true, disableTouchEvent: true, selectedColor: 'blue' }
        }}
      />
      {selected ? (
        <View style={styles.selectedDate}>
          <Text>Selected Date: {selected}</Text>
          <Text style={styles.subtitle}>Available Time Slots:</Text>
          {availableSlots.map((slot) => (
            <Button
              key={slot}
              title={slot}
              onPress={() => bookAppointment(slot)}
            />
          ))}
        </View>
      ) : null}
      <View style={styles.appointmentsListContainer}>
        <Text style={styles.subtitle}>Your Appointments:</Text>
        <FlatList
          data={userAppointments}
          renderItem={renderAppointment}
          keyExtractor={item => item.id}
        />
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    textAlign: 'center',
    marginVertical: 20,
  },
  subtitle: {
    fontSize: 16,
    fontWeight: 'bold',
    marginTop: 10,
    marginBottom: 5,
  },
  selectedDate: {
    marginTop: 20,
    padding: 20,
    alignItems: 'center',
  },
  appointmentsListContainer: {
    marginTop: 20,
    padding: 20,
  },
  appointmentItem: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 10,
    padding: 10,
    borderWidth: 1,
    borderColor: 'gray',
    borderRadius: 5,
  },
});