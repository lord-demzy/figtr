import {
  useForm,
  Controller,
} from "react-hook-form";
import { Label } from "@/components/ui/label";
import { cn } from "@/lib/utils";

const Form = useForm;

interface FormFieldProps {
  control: any;
  name: string;
  render: (props: { field: any; fieldState: any }) => React.ReactNode;
}

function FormField({ control, name, render, ...props }: FormFieldProps) {
  return <Controller control={control} name={name} render={render} {...props} />;
}

function FormItem({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="form-item"
      className={cn("grid gap-1.5", className)}
      {...props}
    />
  );
}

function FormLabel({ className, ...props }: React.ComponentProps<typeof Label>) {
  return <Label data-slot="form-label" className={cn(className)} {...props} />;
}

function FormControl({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="form-control"
      className={cn("relative w-full", className)}
      {...props}
    />
  );
}

function FormDescription({ className, ...props }: React.ComponentProps<"p">) {
  return (
    <p
      data-slot="form-description"
      className={cn("text-sm text-muted-foreground", className)}
      {...props}
    />
  );
}

function FormMessage({ className, ...props }: React.ComponentProps<"p">) {
  return (
    <p
      data-slot="form-message"
      className={cn("text-sm font-medium text-destructive", className)}
      {...props}
    />
  );
}

export {
  Form,
  FormField,
  FormItem,
  FormLabel,
  FormControl,
  FormDescription,
  FormMessage,
};