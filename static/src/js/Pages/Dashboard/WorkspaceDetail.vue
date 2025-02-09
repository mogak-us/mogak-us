<script setup>
import WorkspaceLayout from '@/layouts/WorkspaceLayout.vue';
import MeetupItem from '@/Components/MeetupItem.vue';
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
</script>

<template>
  <WorkspaceLayout :workspace="workspace">
    <div>
      <h2>Meetups</h2>
      <div class="flex flex-col gap-y-4">
        <MeetupItem v-for="meetup in meetups" :key="meetup.id" :workspace="workspace" :meetup="meetup" />
      </div>
    </div>
  </WorkspaceLayout>
</template>
