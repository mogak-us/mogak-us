<script setup>
import WorkspaceLayout from '@/layouts/WorkspaceLayout.vue';
import { ref } from 'vue';

defineProps({
  workspace: {
    type: Object,
    required: true,
    validator: (obj) => 'id' in obj && 'name' in obj,
  },
  meetup: {
    type: Object,
    required: true,
    validator: (obj) => 'id' in obj && 'name' in obj && "date" in obj
  },
});
const tabs = ref(['Attendance', 'Settings', 'Discussion']);
const activeTab = ref('Attendance');

function setActiveTab(tab) {
  activeTab.value = tab;
}
</script>

<template>
  <WorkspaceLayout :workspace="workspace">
    <div class="flex gap-x-4">
      <div class="w-32 aspect-square bg-gray-50 rounded-xl">
      </div>
      <div>
        <p class="font-black"> {{ meetup.name }}</p>
        <p>Date: {{ meetup.date }}</p>
      </div>
    </div>
    <div class="tabs">
      <ul class="flex space-x-4">
        <li v-for="tab in tabs" :key="tab" :class="{ 'font-bold': activeTab === tab }" @click="setActiveTab(tab)">
          {{ tab }}
        </li>
      </ul>
    </div>
    <div v-if="activeTab === 'Attendance'">
      <p>Attendance feature coming soon...</p>
    </div>
    <div v-if="activeTab === 'Settings'">
      <p>Settings feature coming soon...</p>
    </div>
    <div v-if="activeTab === 'Discussion'">
      <p>Discussion feature coming soon...</p>
    </div>
  </WorkspaceLayout>
</template>
