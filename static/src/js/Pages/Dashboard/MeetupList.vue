<script setup>
import MeetupItem from '@/Components/MeetupItem.vue';
import WorkspaceLayout from '@/layouts/WorkspaceLayout.vue';

defineProps({
  workspace: {
    type: Object,
    required: true,
    validator: (obj) => 'id' in obj && 'name' in obj,
  },
  meetups: Array,
});
</script>

<template>
  <WorkspaceLayout :workspace="workspace">
    <div id="meetups" class="grid grid-cols-4 gap-4">
      <div v-for="meetup in meetups" :key="meetup.id">
        <MeetupItem :meetup="meetup" :workspace="workspace" />
      </div>
    </div>
  </WorkspaceLayout>
</template>
