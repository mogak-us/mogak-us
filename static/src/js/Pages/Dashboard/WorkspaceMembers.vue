<script setup lang="ts">
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table'

import { ref, onMounted, defineProps } from 'vue'
import axios from 'axios'

import WorkspaceLayout from '@/layouts/WorkspaceLayout.vue'

const props = defineProps({
  workspace: {
    type: Object,
    required: true,
    validator: (obj) => 'id' in obj && 'name' in obj,
  },
})

const members = ref([])

onMounted(async () => {
  const response = await axios.get(`/api/workspaces/${props.workspace.id}/members/`)
  members.value = response.data
})
</script>

<template>
  <WorkspaceLayout :workspace="workspace">
    <div class="bg-white shadow-md rounded my-6">
      <Table class="min-w-full bg-white">
        <TableCaption class="text-lg font-semibold py-4">Workspace Members</TableCaption>
        <TableHeader>
          <TableRow class="bg-gray-200 text-gray-600 uppercase text-sm leading-normal">
            <TableHead class="py-3 px-6 text-left">ID</TableHead>
            <TableHead class="py-3 px-6 text-left">Alias Name</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody class="text-gray-600 text-sm font-light">
          <TableRow v-for="member in members" :key="member.id" class="border-b border-gray-200 hover:bg-blue-50">
            <TableCell class="py-3 px-6 text-left whitespace-nowrap font-medium">{{ member.id }}</TableCell>
            <TableCell class="py-3 px-6 text-left">{{ member.alias_name }}</TableCell>
          </TableRow>
        </TableBody>
      </Table>
    </div>
  </WorkspaceLayout>
</template>
