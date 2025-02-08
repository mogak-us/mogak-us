<script setup>
import MeetupItem from '@/Components/MeetupItem.vue';

defineProps({
  meetups: Array,
});
</script>

<template>
  <Layout title="Meetups">
    <div v-for="meetup in meetups" :key="meetup.id">
      <MeetupItem :meetup="meetup" />
    </div>
  </Layout>
</template>
