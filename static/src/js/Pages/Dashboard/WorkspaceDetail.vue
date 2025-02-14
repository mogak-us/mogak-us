<script setup>
import axios from 'axios';
import { defineProps, ref } from 'vue';

import WorkspaceLayout from '@/layouts/WorkspaceLayout.vue';
import MeetupItem from '@/Components/MeetupItem.vue';
import Calendar from '@/Components/Calendar.vue';

const props =
  defineProps({
    workspace: {
      type: Object,
      required: true,
      validator: (obj) => 'id' in obj && 'name' in obj,
    },
    meetups: {
      type: Array,
      required: true,
      validator: (arr) => arr.every((obj) => 'id' in obj && 'name' in obj && 'date' in obj),
    },
  });

const statistics = ref({
  totalMeetups: props.meetups.length,
  totalMembers: props.workspace.members.length,
});

const recentActivities = ref([
  { id: 1, description: 'User A joined the workspace' },
  { id: 2, description: 'Meetup B was created' },
]);

const notifications = ref([
  { id: 1, message: 'New meetup scheduled for next week' },
  { id: 2, message: 'Workspace settings updated' },
]);

</script>

<template>
  <WorkspaceLayout :workspace="workspace">
    <div class="p-4 bg-white shadow rounded-lg mb-4">
      <h2 class="text-xl font-bold mb-2">Calendar</h2>
      <Calendar />
    </div>
    <div class="p-4 bg-white shadow rounded-lg mb-4">
      <h2 class="text-xl font-bold mb-2">Meetups</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <MeetupItem v-for="meetup in meetups" :key="meetup.id" :workspace="workspace" :meetup="meetup" />
      </div>
    </div>

    <div class="p-4 bg-white shadow rounded-lg mb-4">
      <h2 class="text-xl font-bold mb-2">Statistics</h2>
      <ul class="list-disc pl-5">
        <li>Total Meetups: {{ statistics.totalMeetups }}</li>
        <li>Total Members: {{ statistics.totalMembers }}</li>
      </ul>
    </div>

    <div class="p-4 bg-white shadow rounded-lg mb-4">
      <h2 class="text-xl font-bold mb-2">Recent Activities</h2>
      <ul class="list-disc pl-5">
        <li v-for="activity in recentActivities" :key="activity.id">
          {{ activity.description }}
        </li>
      </ul>
    </div>

    <div class="p-4 bg-white shadow rounded-lg">
      <h2 class="text-xl font-bold mb-2">Notifications</h2>
      <ul class="list-disc pl-5">
        <li v-for="notification in notifications" :key="notification.id">
          {{ notification.message }}
        </li>
      </ul>
    </div>

  </WorkspaceLayout>
</template>
